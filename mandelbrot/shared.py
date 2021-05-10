import math
import numpy as np
import matplotlib.pyplot as plt
from numba import jit


@jit
def makeImage(array,xmin,xmax,ymin,ymax,step,colorTheme=0):
    """
    Creates a mandelbrot image based on the values of array / step
    I made this a separate function so i could time the computations only
    Args:
        array (ndarray) : 2d array of mandelbrot values
        step (int) : how many steps was used when calculating mandelbrot values
    """
    image = np.zeros((array.shape[0], array.shape[1], 3))
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            v = (array[x,y] / step)
            if colorTheme == 1:
                image[x,y] = getColorSky( v)
            elif colorTheme == 2:
                image[x,y] = getColorGreyscale( v  )
            else:
                image[x,y] = getColorAutumn( v )
    ax = plt.gca()
    return ax.imshow(image, extent=[xmin,xmax,ymin,ymax], interpolation="bicubic")

@jit
def getColor(c):
    """
    Returns a color based on the value of c

    Args:
        c (number) : the number to base the color on
    Returns:
        r,g,b (numbers) : the rgb colors
    """
    g = 0.0
    b = 0.0
    r = 0.0
    if (c < 1.00):
        r = c
        b = math.cos(c * 3)
        g = math.sin(c * 3) 
    return c,g,b

@jit
def conv(n, mi,mx):
    """
    Converts a number between [0,1] to a number between [mi,mx]
    Args:
        n (number): the number between [0,1] to convert
        mi (number): the minimum in the new range
        mx (number): the maximum in the new range
    Returns:
        number : the new number in the range
    """
    r = mx - mi
    return (n * r) + mi
@jit
def getColorAutumn(c):
    """
    Returns a autumn-themed color ( orange, yellow, green ) based on the value of c

    Args:
        c (number) : the number to base the color on
    Returns:
        r,g,b (numbers) : the rgb colors
    """
    g = 0.0
    b = 0.0
    r = 0.0
    if (c < 1.00):
        c = c * 10 # gave me a better result
        x = math.sin(c*2847) * 0.5 + 0.5
        y = math.cos(c * 3764) * 0.5 + 0.5
        z = math.sin(c*4882) * 0.5 + 0.5
        r = conv(x,0.7,1.0)
        g = conv(y,0.3,0.9) * r
        b = conv(z,0.0,0.06)
    return r,g,b

@jit
def getColorGreyscale(c):
    """
    Returns a greyscale based on the value of c

    Args:
        c (number) : the number to base the color on
    Returns:
        r,g,b (numbers) : the rgb colors
    """
    g = 0.0
    b = 0.0
    r = 0.0
    if (c < 1.00):
        c = c * 10
        c = conv(c,0.1,0.9)
        r = c
        g = c
        b = c
    return r,g,b

@jit
def getColorSky(c):
    """
    Returns a sky-themed color ( blue,white ) based on the value of c

    Args:
        c (number) : the number to base the color on
    Returns:
        r,g,b (numbers) : the rgb colors
    """
    g = 0.0
    b = 0.0
    r = 0.0
    if (c < 1.00):
        c = c * 10
        x = math.sin(c*2847) * 0.5 + 0.5
        y = math.sin(c * 3764) * 0.5 + 0.5
        g = conv(y,0.5,0.9)
        r = conv(x,0.0,0.7) * g
        b = 1.0
    return r,g,b