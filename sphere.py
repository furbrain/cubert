import cubertmpl as cubert
import numpy as np
import math
import time
import itertools

DELAY = 0.1

start_time = time.time()

COLOURS = (
    (255, 0, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 255),
    (255, 0, 255),
    (255, 0, 0))

def colour_func(r):
    t = time.time()-start_time
    pos = (r+t/3) % 3.5
    index = int(pos*6.0/3.5)
    offset = (pos*6.0/3.5)- index
    c1 = COLOURS[index]
    c2 = COLOURS[index+1]
    colour = [int(c1[i]*(1.0-offset) + c2[i]*offset) for i in range(3)]
    return colour
    
def subcube_func(x, y, z):
    pos = np.asarray([x,y,z])
    pos  = pos-3.5
    r =np.linalg.norm(pos) 
    if r < 3.5:
        return colour_func(r)
    else:
        return (0,0,0)

cube = cubert.Cubert()
while True:
    cube.clear()
    for i, j, k in itertools.product(range(8), repeat=3):
        cube.set_pixel(i, j, k, subcube_func(i, j, k))
    cube.show()
    time.sleep(DELAY)
