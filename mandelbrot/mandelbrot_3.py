import matplotlib.pyplot as plt
import numpy as np
import shared as sh
import time
from numba import jit,njit,prange




@njit(parallel=True, fastmath=True)
def mandelbrot(c, step):
    """
    Returns how many times it takes to apply c to make it grow towards infinity

    Args:
        c (complex) : the complex number to grow
        step (number) : how many times to try for
    Returns:
        (number) : how many times it took or the escape value
    """
    z = c
    for r in range(step):
        if abs(z) > 2 :
            return r
        z = z ** 2 + c # here i didnt see any noticeable difference between z^2 and z*z
    return step

@njit(parallel=True,fastmath=True)
def mandelbrot_numba(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000):
    """Loops trought the rectangle and calls mandelbrot for each complex pair 
    then populates a 2d array with the result of mandelbrot call

    Args:
        xmin (number): minimum value of the x-axis
        xmax (number): maximum value of the x-axis
        ymin (number): minimum value of the y-axis
        ymax (number): maximum value of the y-axis
        Nx (number): steps on the x-axis (resolution)
        Ny (number): steps on the y-axis (resolution)
        max_escape_time=1000 (number,optional) : how deep to search for a mandelbrot value
    Returns:
        2d array of mandelbrot values
    """
    xAxis = np.linspace(xmin,xmax, Nx) # create a array over the x axis of the image, with Nx as the length of the array
    yAxis = np.linspace(ymin, ymax, Ny)
    i = np.zeros((Nx,Ny))
    for x in prange(Nx): # pylint says this is a error but the program runs fine
        for y in prange(Ny): # i used prange in the hope that numba understands that those loops can be removed for parallelization
            i[x,y] = mandelbrot(complex(xAxis[y],yAxis[x]), max_escape_time)
    return i

# see onrelease() why i have those variables here
cx = 0
cy = 0
xmin = -2.0000
xmax = 1.0000
ymin = -1.50000
ymax = 1.50000
Nx = 1000
Ny = 1000
max_escape_time = 1000
colorTheme = 0

def onclick(event):
    global cx,cy
    cx = event.xdata
    cy = event.ydata
def onrelease(event):
    """ I made a extra function where you can click and drag a box over the image to "zoom" into that box 
    it probably does not work 100% right
    """
    global cx,cy,xmin,xmax,ymin,ymax,Nx,Ny
    xmin = cx if (cx < event.xdata) else event.xdata
    xmax = cx if (cx > event.xdata) else event.xdata
    ymin = cy if (cy > event.ydata) else event.ydata
    ymax = cy if (cy < event.ydata) else event.ydata
    a = mandelbrot_numba(xmin, xmax, ymin, ymax,Nx,Ny)
    sh.makeImage(a,xmin, xmax,ymin,ymax,max_escape_time, colorTheme) # create a new image based on the box
    plt.draw() # update the plot
    plt.savefig("cont.png", bbox_inches='tight')

def enableDrawBoxZoom(x_min,x_max,y_min,y_max,N_x,N_y,escape_time=1000, color_Theme=0):
    """ 
    creates a mandelbrot set that you can zoom in on by dragging a box with the mouse
    """
    global xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time,colorTheme
    xmin = x_min
    xmax = x_max
    ymin = y_min
    ymax = y_max
    Nx = N_x
    Ny = N_y
    max_escape_time = escape_time
    colorTheme = color_Theme
    array = mandelbrot_numba(xmin, xmax,ymin,ymax,Nx,Ny,max_escape_time)
    sh.makeImage(array,xmin, xmax,ymin,ymax,max_escape_time, colorTheme)
    fig = plt.gcf()
    fig.canvas.mpl_connect('button_press_event', onclick)
    fig.canvas.mpl_connect('button_release_event', onrelease)
    plt.show()

