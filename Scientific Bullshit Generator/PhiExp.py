import os, re
import random,readJSON

data = readJSON.读JSON文件("PEdata.json")
名人名言 = data["famous"] # a 代表前面垫话，b代表后面垫话
前面垫话 = data["before"] # 在名人名言前面弄点废话
后面垫话 = data['after']  # 在名人名言后面弄点废话
废话 = data['bosh'] # 代表文章主要废话来源
one = data['one']
方圆十里的=data['方圆十里的']
电子科技大学的=data['电子科技大学的']
成语=data['成语']
乡亲们=data['乡亲们']
奇怪=data['奇怪']
唉=data['唉']
xx = "学生会退会"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace("a",random.choice(前面垫话) )
    xx = xx.replace("b","" )
    return xx

def writeone():
    global writeone
    xx=next(writeone)

def 另起一段():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":

    xx = input("请输入想说的话:")
    (who,what)=xx.split('真',1);
    i=0;
    while(i<5):
        tmp = str()
        # tmp+=random.choice(one)
        tmp+=来点名人名言()
        tmp=tmp+'而'+who+random.choice(成语)+','+random.choice(成语)+','
        sign=random.randint(0,1)
        if sign:
            tmp=tmp+'却如此'+what+'。'
        else:
            tmp=tmp+random.choice(方圆十里的)+random.choice(乡亲们)+'没有觉得不'+what+'的。'
        sign=random.randint(0,2)
        if sign==0:
            tmp=tmp+'这难道是合理的吗？'
        elif sign==1:
            tmp=tmp+who+'难道不觉得'+random.choice(奇怪)+'吗？'
        else:
            tmp=tmp+random.choice(唉)
        sign=random.randint(0,2)
        if sign==0:
            tmp+='这大概就是人生吧！'
        elif sign==0:
            tmp+='难道这世间本就该如此吗？'
        else:
            tmp=tmp+'这难道就是'+random.choice(乡亲们)+'所说的'+what+'之王吗？'
        print(tmp)
        i+=1

