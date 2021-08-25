from PIL import Image

im = Image.open('RUC_0.jpeg')#读取图片
im = im.convert('RGBA')#转化成RGBA（RBG+透明度）格式
pix = im.load()
width = im.size[0]
height = im.size[1]

for x in range(width):
    for y in range(height):
        r, g, b, a = pix[x, y]
        if (r>250)&(g>250)&(b>250):  #如果是白色
             # r=0
             # g=0
             # b=0
            a=0
        # else:
        #     r=255
        #     g=255
        #     b=255
        im.putpixel((x,y),(r,g,b,a))  #把四个参数还给这个像素​

    im.save("RUC2.PNG")  #保存
