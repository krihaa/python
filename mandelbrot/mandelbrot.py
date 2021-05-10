import argparse
import mandelbrot_1 as mb1
import mandelbrot_2 as mb2
import mandelbrot_3 as mb3
import shared as sh
import matplotlib.pyplot as plt
import time
parser = argparse.ArgumentParser(description='Creates a mandelbrot image.')
parser.add_argument("xmin", type=float,
                    help='bottom x axis')
parser.add_argument("xmax", type=float,
                    help='top x axis')
parser.add_argument("ymin", type=float,
                    help='bottom y axis')
parser.add_argument("ymax", type=float,
                    help='top y axis')
parser.add_argument("Nx", type=int,
                    help='resolution on the x-axis')
parser.add_argument("Ny", type=int,
                    help='resolution on the y-axis')
parser.add_argument("step", type=int,
                    help='max escape time')
parser.add_argument("filename", help='name of the output file')
parser.add_argument("-s",action="store_true", help='Show the finished image')
parser.add_argument("-u", type=int, choices=[0, 1, 2],
                    help="Pick between implementations: 0: Python, 1: Numpy, 2: Numba (Default: 0)")
parser.add_argument("-c", type=int, choices=[0, 1, 2],
                    help="Pick between 3 color themes: 0: Autumn, 1: Sky, 2: Greyscale (Default: 0)")
parser.add_argument("-z", action="store_true", help="Creates a mandelbrot at [-2,1] [-1.5,1.5] that you can zoom in on by drawing a box with your mouse")

args = parser.parse_args()
array = 0

if args.z:
    mb3.enableDrawBoxZoom(args.xmin, args.xmax,args.ymin,args.ymax,args.Nx,args.Ny, args.step, args.c)
else:
    if args.u == 1:
        t0 = time.time()
        array = mb2.mandelbrot_numpy(args.xmin, args.xmax,args.ymin,args.ymax,args.Nx,args.Ny, args.step)
        print("it took: %s seconds to compute with numpy" % (time.time() - t0))
    elif args.u == 2:
        t0 = time.time()
        array = mb3.mandelbrot_numba(args.xmin, args.xmax,args.ymin,args.ymax,args.Nx,args.Ny, args.step)
        print("it took: %s seconds to compute with numba" % (time.time() - t0))
    else:
        t0 = time.time()
        array = mb1.mandelbrot_python(args.xmin, args.xmax,args.ymin,args.ymax,args.Nx,args.Ny, args.step)
        print("it took: %s seconds to compute with python" % (time.time() - t0))

    sh.makeImage(array,args.xmin, args.xmax,args.ymin,args.ymax,args.step, args.c)
    fig = plt.gcf()
    plt.savefig(args.filename, dpi=400, bbox_inches='tight')
    if args.s:
        plt.show()


# i dont understand in what file you want this
def compute_mandelbrot(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time=1000, plot_filename=None):
    array = mb3.mandelbrot_numba(xmin,xmax,ymin,ymax,Nx,Ny,max_escape_time)
    if plot_filename is not None:
        sh.makeImage(array,xmin,xmax,ymin,ymax, max_escape_time)
        plt.savefig(plot_filename, dpi=400, bbox_inches='tight')
    return array