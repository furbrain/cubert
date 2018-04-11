import neopixel

class Cubert(object):
    """Interface to control a 8x8x8 RGB cube (or simulation thereof)"""
    LED_COUNT   = 512      # Number of LED pixels.
    LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
    LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)

    def __init__(self):
    
        # Create NeoPixel object with appropriate configuration.
        self.strip = neopixel.Adafruit_NeoPixel(cls.LED_COUNT, cls.LED_PIN, cls.LED_FREQ_HZ, cls.LED_DMA, cls.LED_INVERT)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    def show(self):
        """Make any changes on the cube visible"""
        self.strip.show()
                
    def get_pixel_index(self, x, y, z):
        if z % 2:
            x = 7-x
        if x % 2:
            y = 7-y
        return y + x*8 + z*64        return y + x*8 + z*64
        
    def set_pixel(self, x, y, z, colour):
        """Set the pixel at x,y,z to the colour specified. colour should be a tuple of integers
        representing red, green and blue respectively, with a maximum of 255.
        Call show after you have finished making changes to make them visible on your cube"""
        index = self.get_pixel_index(x, y, z)
        self.strip.setPixelColor(index, neopixel.Color(*colour))
        
    def clear(self):
        """Set all pixels to black (0,0,0).
        Call show after you have finished making changes to make them visible"""
        self.strip.clear()        
        
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
