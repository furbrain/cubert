import cubertmaya as cubert
import random
import time

RAIN_DENSITY=0.80

class Raindrop(object):
    COLORS = [(255,255,255), 
              (192, 192, 192),
              (128, 128, 128),
              (64, 64, 64)]
    def __init__(self, cube):
        self.x = random.randint(0,7)
        self.z = random.randint(0,7)
        self.pos = 7
        self.cube = cube
        
    def animate(self):
        for i, col in enumerate(self.COLORS):
            y = self.pos+i
            if 0 <= y <= 7:
                self.cube.set_pixel(self.x, y, self.z, col)
        self.pos -=1
                
    def dead(self):
        return self.pos < -len(self.COLORS)

cube = cubert.Cubert()
    
drops = []
while True:
    time.sleep(0.05)
    cube.clear()
    if random.random()< RAIN_DENSITY:
        drops.append(Raindrop(cube))
    for drop in drops:
        drop.animate()
    drops = [drop for drop in drops if not drop.dead()]
    cube.show()
