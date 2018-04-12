import cubertmpl as cubert
import numpy as np
import math
import time
import itertools

DELAY = 0.1
axis = [2,3,4]
axis = np.asarray(axis)
axis = axis/math.sqrt(np.dot(axis, axis))

start_time = time.time()

COLOURS = (
    (255, 0, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 255),
    (255, 0, 255),
    (255, 0, 0))

def colour_func(x, y, z):
    pos = x+y+z
    index = int(pos*6.0/16)
    offset = (pos*6.0/16)- index
    c1 = COLOURS[index]
    c2 = COLOURS[index+1]
    colour = [int(c1[i]*(1.0-offset) + c2[i]*offset) for i in range(3)]
    return colour
    
def subcube_func(x, y, z):
    t = time.time()-start_time
    theta = t/10
    a = math.cos(theta/2.0)
    b, c, d = -axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    mat = np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])
    pos = np.asarray([x-3.5, y-3.5, z-3.5])
    new_pos = np.dot(mat, pos)
    if all(-2 <x < 2 for x in new_pos):
        return colour_func(*(new_pos+2))
    else:
        return (0,0,0)

cube = cubert.Cubert()
while True:
    cube.clear()
    for i, j, k in itertools.product(range(8), repeat=3):
        cube.set_pixel(i, j, k, subcube_func(i, j, k))
    cube.show()
    time.sleep(DELAY)
