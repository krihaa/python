import matplotlib.pyplot as plt
import numpy as np
import shared as sh
import time


def mandelbrot(c, step):
    """
    Returns how many times it takes to apply c to make it grow towards infinity

    Args:
        c (complex) : the complex number to grow
        step (number) : how many times to try for
    Returns:
        (number) : how many times it took or the escape value
    """
    z = c # i am skipping f(0) because 0^2 + c = c and abs(0) > 2 is always false so its pointless to have it
    for r in range(step):
        if abs(z) > 2 :
            return r
        z = z * z + c   # i almost halfed my execution time changing from z = z^2+c to z=z*z+c
    return step
def mandelbrot_python(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000):
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
    xAxis = np.linspace(xmin,xmax, Nx)
    yAxis = np.linspace(ymin,ymax, Ny)
    i = np.empty((Nx,Ny))
    for x in range(Nx):
        for y in range(Ny):
            i[x,y] = mandelbrot(complex(xAxis[y],yAxis[x]), max_escape_time)
    return i