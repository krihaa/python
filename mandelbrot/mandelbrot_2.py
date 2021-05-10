import matplotlib.pyplot as plt
import numpy as np
import shared as sh
import time
def mandelbrot_numpy(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000):
    """ 
    Uses numpy to populate a array for mandelbrot values 
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
    yAxis = np.linspace(ymin,ymax, Ny)
    c = xAxis + yAxis[:,None] * 1j # turn it into a 2d array
    z = c.copy() # skipping f(0)
    i = np.zeros_like(c ,dtype=int)
    for r in range(max_escape_time):
        j = np.less_equal(np.abs(z), 2) # j here works like a if-check for every element in the array
        i[j] = r+1
        z[j] = z[j] ** 2 + c[j]
    return i