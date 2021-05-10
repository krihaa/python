from setuptools import setup

setup(
   name='Mandelbrot',
   version='1.0',
   description='Creates mandelbrot images',
   packages=['mandelbrot'],
   install_requires=[
          'numpy',
          'numba',
          'matplotlib',
      ],
)