from casioplot import *
from math import ceil

black = (0,)*3


def interpolate(colors, nbValues):
  length = ceil(nbValues / (len(colors)-1))
  dColors = [tuple([(colors[i+1][j] - colors[i][j])/length for j in [0,1,2]]) for i in range(len(colors)-1)]
  
  return lambda x: [ceil(colors[x%(length*(len(colors)-1))//length][j] + (dColors[x%(length*(len(colors)-1))//length][j] * (x%(length*(len(colors)-1))-(x%(length*(len(colors)-1))//length*length)))) for j in [0,1,2]]
  
def linspace(Range, values):
  a = (Range[1]-Range[0])/values
  return [Range[0]+a*i for i in range(values)]

def lim(c, maxIteration):
  z = c
  for iteration in range(maxIteration):
    z = z**2 + c
    
    if abs(z) > 2:
      return iteration
      
  return maxIteration

def mandelbrot(x,y,maxIteration):
  c = x+y*1j
  
  return maxIteration if x < abs(c-0.25) - 2*abs(c-0.25)**2 + 0.25 or abs(c+1) < 0.25 else lim(c,maxIteration)
  
def ensembleMandelbrot(Xrange,Yrange,length,maxIteration,palette):
  X = linspace(Xrange,length[0])
  Y = linspace(Yrange,length[1])
  
  for pixel in range(length[0]*length[1]):
    x,y = pixel%length[0],pixel//length[0]
    
    iteration = mandelbrot(X[x],Y[y],maxIteration)
      
    set_pixel(x,y,black if iteration == maxIteration else palette(iteration))
        
    show_screen()


Xrange, Yrange = (-4.2,1.2),(-1.2,1.2)
length = (384,192)
maxIteration = 255

palette = interpolate([(0,0,0),(255,0,0),(255,255,0),(0,255,0),(0,255,255),(0,0,255),(255,0,255),(255,0,0),(0,0,0)],255)

ensembleMandelbrot(Xrange, Yrange, length, maxIteration, palette) 