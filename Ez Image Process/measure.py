from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy


im = Image.open('zzcc1.jpg')
pix = im.load()
width = im.size[0]
height = im.size[1]

art=1
art2=art*art

Rmax=-1
Gmax=-1
Bmax=-1
Rmin=256
Gmin=256
Bmin=256

for xx in range(width//art):
    for yy in range(height//art):
        R=0
        G=0
        B=0
        for x in range(xx*art,(xx+1)*art):
            for y in range(yy*art,(yy+1)*art):
                r, g, b = pix[x, y]
                R+=r
                G+=g
                B+=b
        R//=art2
        G//=art2
        B//=art2
        Rmax=R if R>Rmax else Rmax
        Gmax=G if G>Gmax else Gmax
        Bmax=B if B>Bmax else Bmax
        Rmin=R if R<Rmin else Rmin
        Gmin=G if G<Gmin else Gmin
        Bmin=B if B<Bmin else Bmin
print([Rmin,Rmax])
print([Gmin,Gmax])
print([Bmin,Bmax])
