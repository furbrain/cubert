import cubertmpl as cubert
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

def colour_func(x, y, z):
    t = time.time()-start_time
    pos = (x+y+z+t) % 21
    index = int(pos*6.0/21)
    offset = (pos*6.0/21)- index
    c1 = COLOURS[index]
    c2 = COLOURS[index+1]
    colour = [c1[i]*(1.0-offset) + c2[i]*offset for i in range(3)]
    return colour

cube = cubert.Cubert()
while True:
    cube.clear()
    for i, j, k in itertools.product(range(8), repeat=3):
        cube.set_pixel(i, j, k, colour_func(i, j, k))
    cube.show()
    time.sleep(DELAY)
