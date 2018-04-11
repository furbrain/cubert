Cubert
======

This is some software to test out code for controlling [Cubert](https://lorrainbow.wordpress.com/cube), an 8x8x8 RGB led cube. 
To use the simulator, you will need [MayaVi](http://docs.enthought.com/mayavi/mayavi/index.html) (preferred) or [Matplotlib](https://matplotlib.org) installed.

Usage
-----
The first step is to import the cubert library

MayaVi:
```import cubertmaya as cubert```

Matplotlib:
```import cubertmpl as cubert```

Running on actual cubert:
```import cubert as cubert```

Next create a `Cubert` instance: ```cube = cubert.Cubert()```

Set a pixel at X:3, Y:4, Z:5 to green:
```cube.set_pixel_color(3,4,5, (0, 255, 0))```

After changing any pixels, you then need to call
```cube.show()```

To set all pixels to off, call
```cube.clear()```

