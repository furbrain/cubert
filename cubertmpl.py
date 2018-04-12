import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Cubert(object):
    """Interface to control a 8x8x8 RGB cube (or simulation thereof)"""
    def __init__(self):
        plt.ion()
        self.xs, self.ys, self.zs = [i.flatten() for i in np.mgrid[0:8:1, 0:8:1, 0:8:1]]
        self.fig = plt.figure()
        self.fig.patch.set_facecolor("black")
        self.ax = Axes3D(self.fig)
        self.ax.set_axis_off()
        self.ax.set_facecolor("black")
        self.ax.view_init(24,-124)
        self.ax.set_aspect("equal")
        self.data = [(0.1,0.1,0.1,0.75)]*512
        
    def show(self):
        """Make any changes on the cube visible"""
        self.ax.clear()
        self.scatter = self.ax.scatter(self.xs, self.ys, self.zs, c= self.data)
        self.ax.set_axis_off()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.draw()
        
    def get_pixel_index(self, x, y, z):
        return y + x*64 + z*8
        
    def set_pixel(self, x, y, z, colour):
        """Set the pixel at x,y,z to the colour specified. colour should be a tuple of integers
        representing red, green and blue respectively, with a maximum of 255.
        Call show after you have finished making changes to make them visible on your cube"""
        colour = [0.1+0.9*(i/255.0)  for i in colour]
        self.data[self.get_pixel_index(x, y, z)] = colour
        
    def clear(self):
        self.data[:] = [(0.1,0.1,0.1,0.75)] * 512
        
        
if __name__=="__main__":
    import time
    c = Cubert()
    c.show()
    time.sleep(1)
    c.clear()
    for k in range(8):
        for i in range(8):
            for j in range(8):
                c.set_pixel(i,j,k,(1,0,0))
        c.show()
    time.sleep(1)
