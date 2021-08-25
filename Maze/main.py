# rectangle maze
import random,math,copy
from PIL import Image
# show the maze or the path
def show_maze(maze):
    for i in maze:
        for j in i:
            if j=='0':  # wall
                print('\033[36m',j,sep='',end='\033[0m')
            elif j=='O':  # [ entrance & exit ]& path
                print('\033[33m',j,sep='',end='\033[0m')
            elif j=='X':  # footprint
                print('\033[31m',' ',sep='',end='\033[0m')
            else:
                print(j,end='')
        print()

# route optimization
def optimize(path):
    # anterior step, next step, posterior step
    anterior=0
    while anterior<len(path):
        x,y=path[anterior]
        next_step=[(x,y-1),(x-1,y),(x,y+1),(x+1,y)]
        for posterior in range(len(path)-1,anterior+1,-1):
            if path[posterior] in next_step:
                del path[anterior+1:posterior]
                break
        anterior+=1
# find the exit of the maze
def route(maze,height,width,option=0):
    if option==0:
        # right down up left
        steps=((0,1),(1,0),(-1,0),(0,-1))
    elif option==1:
        # right up down left
        steps=((0,1),(-1,0),(1,0),(0,-1))
    else:
        # left up down right
        steps=((0,-1),(-1,0),(1,0),(0,1))
    # the way out of maze
    path=[(1,1)]
    # never again
    footprint=[]
    # entrance
    x=y=1
    while x!=height-2 or y!=width-2:
        # horizontal vertical
        for h,v in steps:
            if maze[x+h][y+v]==' ' and (x+h,y+v) not in footprint:
                path.append((x+h,y+v))
                footprint.append((x+h,y+v))
                break
        else:
            if path:
                path.pop()
            else:
                # There is no escape. show the maze and footprint
                for x,y in footprint:
                    maze[x][y]='X'
                show_maze(maze)
                break
        # location
        if path:
            x,y=path[-1]
    else:
        # show the maze, footprint and path
        for x,y in footprint:
            maze[x][y]='X'
        # optimize the path of maze
        optimize(path)
        for x,y in path:
            maze[x][y]='O'


        show_maze(maze)
# play
if __name__ == "__main__":

    im = Image.open('migong1.jpg')
    im = im.convert('RGBA')
    pix = im.load()
    width = im.size[0]
    height = im.size[1]



    global core
    core=[]
    for i in range (height):
        core.append([])
        for j in range(width):
            core[i].append(' ')

    for y in range(height-10):
        for x in range(width-14):
            r, g, b, a = pix[x, y]
            if(r<150)&(g<150):
                core[y][x]='0'

    for i in range(10,width-13):
        core[4][i]='0'
        core[height-10][i]='0'
    for i in range(4,height-9):
        core[i][10]='0'
        core[i][width-14]='0'

    global Maze
    Maze=[]
    for i in range(height-13):
        Maze.append([])
        for j in range(width-23):
            Maze[i].append(core[i+4][j+10])
    Maze[0][0]='O'
    Maze[height-14][width-24]='O'
    # for i in range(width-12):
    #     Maze[0][i]='0'
    #     Maze[height-9]='0'
    # for i in range(height-8):
    #     Maze[i][0]='0'
    #     Maze[i][width-13]='0'
    # Maze[0][0]='O'
    # Maze[height-9][width-13]='O'
    # for y in range(1,height-7):
    #     for x in range(1,width-11):
    #         Maze[y][x]=core[y-1][x-1]
    route(Maze,height-13,width-23)


    im = Image.open('迷宫.jpg')
    im = im.convert('RGBA')
    pix = im.load()
    w = im.size[0]
    h = im.size[1]

    for y in range(4,h-9):
        for x in range(10,w-13):
            r, g, b, a = pix[x, y]
            if Maze[y-4][x-10]=='O':
                r=0
                g=250
                b=154
            elif Maze[y-4][x-10]=='X':
                r=255
                g=99
                b=71
                a=150
            im.putpixel((x,y),(r,g,b,a))
    im.save("R5.PNG")
