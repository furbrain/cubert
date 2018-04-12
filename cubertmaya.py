import numpy as np
import itertools
import threading
import time

OPACITY = 192

class Cubert(object):
    """Interface to control a 8x8x8 RGB cube (or simulation thereof)"""
    def __init__(self):
        self.colormap = [[20,20,20, OPACITY]] * 512
        self.thread = threading.Thread(target=self._mlab_init)
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
        mlab.view(127,24, distance="auto")
        mlab.roll(0)
        self.points.module_manager.scalar_lut_manager.lut.table = self.colormap
        self.gui = GUI
        mlab.show()
       
    def _mlab_show(self):
        self.points.module_manager.scalar_lut_manager.lut.table = self.colormap
        self.mlab.draw()
                    
    def show(self):
        """Make any changes on the cube visible"""
        if hasattr(self,'gui'):
            self.gui.invoke_later(self._mlab_show)
        
    def _get_pixel_index(self, x, y, z):
        return x*64 + y*8 + 7-z
        
    def set_pixel(self, x, y, z, colour):
        """Set the pixel at x,y,z to the colour specified. colour should be a tuple of integers
        representing red, green and blue respectively, with a maximum of 255.
        Call show after you have finished making changes to make them visible on your cube"""
        colour = [20+int((i*235)/255) for i in colour]  + [OPACITY]
        self.colormap[self._get_pixel_index(x, y, z)] = colour
        
    def clear(self):
        """Set all pixels to black (0,0,0).
        Call show after you have finished making changes to make them visible"""
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
