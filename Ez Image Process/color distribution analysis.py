from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy

matrix=[]
for i in range(85):
    matrix.append([])
    for j in range(85):
        matrix[i].append([])
        for k in range(85):
            matrix[i][j].append(0)

im = Image.open('detect.jpg')
im = im.convert('RGBA')
pix = im.load()
width = im.size[0]
height = im.size[1]

art=10
art2=art*art

# npic=[]
# for i in range(width//art):
#     npic.append([])
#     for j in range(height//art):
#         npic[i].append([])
#         for k in range(3):
#             npic[k].append([])

pur=153/255
matmax=0

for xx in range(width//art):
    for yy in range(height//art):
        R=0
        G=0
        B=0
        for x in range(xx*art,(xx+1)*art):
            for y in range(yy*art,(yy+1)*art):
                r, g, b, a = pix[x, y]
                R+=r
                G+=g
                B+=b
        R//=art2
        G//=art2
        B//=art2
        matrix[R//4][G//4][B//4]+=1
        if matrix[R//4][G//4][B//4]>matmax:
            matmax=matrix[R//4][G//4][B//4]
# print(matmax)

ax = plt.figure().add_subplot(111, projection = '3d')
for x in range(85):
    for y in range(85):
        for z in range(85):
            if matrix[x][y][z]:
                if (y>54)&(z>32):
                    pass
                else:
                    ax.scatter(x,y,z,s=12,facecolor=[x*3/255,y*3/255,z*3/255],edgecolors=[x*3/255,y*3/255,z*3/255],alpha=(matrix[x][y][z]/matmax)**0.25)
# ax.scatter(xs, ys, zs, facecolors=rgb)

ax1=ax.set_xlabel('R//4')
ax2=ax.set_ylabel('G//4')
ax3=ax.set_zlabel('B//4')


plt.show()

ax = plt.figure().add_subplot(111, projection = '3d')

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
