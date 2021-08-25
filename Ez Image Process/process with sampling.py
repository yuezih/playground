from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy

global matrix
matrix=[]
for i in range(256):
    matrix.append([])
    for j in range(256):
        matrix[i].append([])
        for k in range(256):
            matrix[i][j].append(0)

global art
global art2
art=1
art2=art*art

def learn(str):
    im = Image.open(str)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
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
            matrix[R][G][B]=1

if __name__ == "__main__":

    learn('wxq1.jpg')
    learn('wxq2.jpg')
    # learn('5.jpg')
    # learn('3.jpg')
    # learn('4.jpg')

    im = Image.open('wanxingqun.jpg')
    im = im.convert('RGBA')
    pix = im.load()
    width = im.size[0]
    height = im.size[1]

    art=1
    art2=art*art

    # npic=[]
    # for i in range(width//art):
    #     npic.append([])
    #     for j in range(height//art):
    #         npic[i].append([])
    #         for k in range(3):
    #             npic[k].append([])

    dim=50

    for xx in range(width//art):
        for yy in range(height//art):
            R=0
            G=0
            B=0
            for x in range(xx*art,(xx+1)*art):
                for y in range(yy*art,(yy+1)*art):
                    r, g, b, a = pix[x, y]
                    # color = im.getpixel((x,y))
                    # print(b)
                    R+=r
                    G+=g
                    B+=b
            R//=art2
            G//=art2
            B//=art2

            sign1=0
            sign2=0
            sign3=0

            for i in range (max(0,R-dim),min(255,R+dim)):
                sign1+=matrix[i][G][B]
            for i in range (max(0,G-dim),min(255,G+dim)):
                sign2+=matrix[R][i][B]
            for i in range (max(0,B-dim),min(255,B+dim)):
                sign3+=matrix[R][G][i]

            # if (R>200)&(G>200):
            #     a=0

            if sign1+sign2+sign3:
                # R=255
                # G=255
                # B=255
                a=0
            elif r<20:
                R=255
                G=255
                B=255

    #         # npic[xx][yy][0]=R
    #         # npic[xx][yy][1]=G
    #         # npic[xx][yy][2]=B
    #         # if color[1]<30&color[2]<0:
    # #             color = color[:-1] + (0, )
            for x in range(xx*art,(xx+1)*art):
                for y in range(yy*art,(yy+1)*art):
                    im.putpixel((x,y),(R,G,B,a))
    #         a=0
    im.save("wanxingqun1.PNG")
    # # xs=[i for i in range(256)]
    # # ys=[i for i in range(256)]
    # # zs=[i for i in range(256)]
    # # rgb = numpy.random.random((5,3))
    # # print(rgb)
