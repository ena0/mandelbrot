from casioplot import *
from math import ceil

black = (0,)*3


def linspace(Range, values):
  a = (Range[1]-Range[0])/values
  return [Range[0]+a*i for i in range(values)]

def lim(c, maxIteration):
  z = c
  for iteration in range(maxIteration):
    z = z**2 + c
    
    if abs(z) > 2:
      return True
      
  return False

def mandelbrot(x,y,maxIteration):
  c = x+y*1j
  
  return False if x < abs(c-0.25) - 2*abs(c-0.25)**2 + 0.25 or abs(c+1) < 0.25 else lim(c,maxIteration)
  
def ensembleMandelbrot(Xrange,Yrange,length,maxIteration):
  X = linspace(Xrange,length[0])
  Y = linspace(Yrange,length[1])
  
  for pixel in range(length[0]*length[1]):
    x,y = pixel%length[0],pixel//length[0]
    
    iteration = mandelbrot(X[x],Y[y],maxIteration)
      
    if iteration:
      set_pixel(x,y,black)
        
      show_screen()


Xrange, Yrange = (-4.2,1.2),(-1.2,1.2)
length = (128,64)
maxIteration = 255

ensembleMandelbrot(Xrange, Yrange, length, maxIteration) 