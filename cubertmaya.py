import numpy as np
import itertools
import threading
import time

OPACITY = 192

class Cubert(object):
    def __init__(self):
        self.colormap = [[20,20,20, OPACITY]] * 512
        self.thread = threading.Thread(target=self.mlab_init)
        self.thread.start()
        self.show()
       
       
    #these two functions should only be called from within self.thread   
    def _mlab_init(self): 
        import mayavi.mlab as mlab
        from pyface.api import GUI
        self.mlab = mlab
        mlab.figure(bgcolor=(0,0,0))
        x, y, z = [i.flatten() for i in np.mgrid[0:8:1, 0:8:1, 0:8:1]]
        self.points = mlab.points3d(x, y, z, list(range(512)), scale_mode="none", scale_factor=0.4)
        self.points.module_manager.scalar_lut_manager.lut.table = self.colormap
        self.gui = GUI
        mlab.show()
       
    def _mlab_show(self):
        self.points.module_manager.scalar_lut_manager.lut.table = self.colormap
        self.mlab.draw()
                    
    def show(self):
        if hasattr(self,'gui'):
            self.gui.invoke_later(self.mlab_show)
        
    def get_pixel_index(self, x, y, z):
        return y + x*8 + z*64
        
    def set_pixel(self, x, y, z, colour):
        colour = [20+int((i*235)/255) for i in colour]  + [OPACITY]
        self.colormap[self.get_pixel_index(x, y, z)] = colour
        
    def clear(self):
        self.colormap[:] = [[20,20,20,OPACITY]] * 512
        
        
if __name__=="__main__":
    import time
    c = Cubert()
    c.show()
    time.sleep(1)
    c.clear()
    for k in range(8):
        for i in range(8):
            for j in range(8):
                c.set_pixel(i,j,k,(255,0,0))
        time.sleep(1)
        c.show()
    time.sleep(1)
