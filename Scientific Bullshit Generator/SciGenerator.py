import os, re
import random,readJSON

data = readJSON.读JSON文件("articledata.json")
引用 = data["famous"]
说 = data["before"]
说完 = data['after']
废话 = data['bosh']
近年来 = data["近年来"]
很重要 = data["很重要"]
很多研究 = data["很多研究"]
没有进展 = data["没有进展"]
他们的问题 = data["他们的问题"]
我们分析 = data["我们分析"]
我们怎么做 = data["我们怎么做"]
得到了什么结果 = data["得到了什么结果"]
混淆的实验结果 = data["混淆的实验结果"]
研究目的 = data["研究目的"]
我们怎么研究 = data["我们怎么研究"]
研究成果 = data["研究成果"]
填补了怎样的空缺 = data["填补了怎样的空缺"]
做出了怎样的贡献 = data["做出了怎样的贡献"]
废话结尾=data["bosh2"]
xx = "SBIdata"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句废话 = 洗牌遍历(废话)
下一句引用 = 洗牌遍历(引用)


def 来点引用():
    global 下一句引用
    xx = next(下一句引用)
    xx = xx.replace("SHUO",random.choice(说))
    xx = xx.replace("WAN",random.choice(说完))
    return xx

def 来点(列表,课题):
    内容=list(列表)
    句子=random.choice(内容)
    列表.remove(句子)
    try:
        句子=句子.replace("X",课题)
    except:
        pass
    句子=句子.capitalize()
    return 句子

def 另起一段():
    xx = str()
    xx += "\r\n"
    xx += "     "
    return xx

if __name__ == "__main__":
    X=input("请输入研究课题:")
    print('Abstract:',end='\n     ');
    abstract=str()
    abstract=abstract+来点(近年来,X)+来点(很重要,X)+来点(很多研究,X)+来点(没有进展,X)+来点(他们的问题,X)+来点(我们分析,X)+来点(我们怎么做,X)+来点(得到了什么结果,X)
    print(abstract)
    print('1 Introduction',end='\n     ')
    introduction=str()
    introduction=introduction+来点(很重要,X)+来点(很多研究,X)+来点(没有进展,X)+来点(他们的问题,X)+来点(混淆的实验结果,X)+来点(研究目的,X)+来点(我们怎么研究,X)+来点(研究成果,X)+来点(填补了怎样的空缺,X)+来点(做出了怎样的贡献,X)
    print(introduction)
    print('2 Literature Review',end='\n     ')
    literature=str()
    literature=literature+来点(很多研究,X)

    while ( len(literature) < 6000 ) :
        分支 = random.randint(0,100)
        if 分支 < 5:
            literature+=random.choice(废话结尾)
            literature+=另起一段()
        elif 分支 < 20 :
            literature+=来点引用()
        else:
            literature+=next(下一句废话)
    try:
        literature=literature.replace("X",X)
    except:
        pass
    literature+=random.choice(废话结尾)
    print(literature)
