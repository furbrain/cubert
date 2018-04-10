import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Cubert(object):
    def __init__(self):
        plt.ion()
        self.xs, self.ys, self.zs = [i.flatten() for i in np.mgrid[0:8:1, 0:8:1, 0:8:1]]
        self.fig = plt.figure()
        self.fig.patch.set_facecolor("black")
        self.ax = Axes3D(self.fig)
        self.ax.set_axis_off()
        self.ax.set_facecolor("black")
        self.data = [(0.1,0.1,0.1,0.75)]*512
        
        
    def show(self):
        self.ax.clear()
        self.scatter = self.ax.scatter(self.xs, self.ys, self.zs, c= self.data)
        self.ax.set_axis_off()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.draw()
        
    def get_pixel_index(self, x, y, z):
        return y + x*8 + z*64
        
    def set_pixel(self, x, y, z, colour):
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
