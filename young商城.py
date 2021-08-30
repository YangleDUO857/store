#1.准备商品
shop = [
    ["小米11Pro",5000],
    ["iPhone12Pro",7500],
    ["vivox60",3500],
    ["可乐",3],
    ["西瓜",20],
    ["老干妈",15],
    ["卫龙辣条",4],
    ["笔记本",3],
]
#2.准备足够多的钱
money = input("(来啦~铁汁~看看要买点啥啊！)请输入你的总钱数:")
money = int(money)

#3.准备足够空的购物车
mycart = []

#4.输入打折的商品及折数
import random
num=random.randint(1,45)
if num==1 or num==2 or num==3 or num==4 or num==5 or num==6 or num==7 or num==8 or num==9 or num==10:
    print("你获得一张小米11Pro优惠券")
elif num==11 or num==12 or num==13 or num==14 or num==15 or num==16 or num==17 or num==18 or num==19 or num==20 or num==21 or num==22 or num==23 or num==24 or num==25 or num==26 or num==27 or num==28 or num==29 or num==30:
    print ("你获得一张老干妈优惠券")
else:
    print ("你获得一张辣条的优惠券")

#5.开始购物
while True:
    for key,value in enumerate(shop):
        print(key,value)
    print("注：优惠卷编码号 1 小米11Pro 2 老干妈 3 辣条 4 无")
    l = input("输入获得的优惠卷编码号")
    l = int(l)
    if l == 1:
        k = 0.9
    elif l == 2:
        k = 0.1
    elif l == 3:
        k = 0.2
    else:
        k = 0
    '''elif l == 'q' or l == 'Q':
        print("欢迎下次光临！拜拜了您嘞！")
        break'''
        #输入
    chose = input("请输入你想要的商品编号:")
    if chose.isdigit():
        chose = int(chose)
        #商品是否存在
        if chose > len(shop):
            print("对不起，你输入的商品也不存在啊！咋回事儿啊，铁汁！")
        else:
            #金钱是否足够
            if money < shop[chose][1]:
                print("对不起(＞人＜），铁汁你的余额不足，不能购买！")
            else:
                mycart.append(shop[chose])
                if chose == 0 and k == 0.9:
                    mycart.append(shop[chose])
                    print(chose)
                    money = money - k * shop[chose][1]
                    print("恭喜，成功添加购物车!,您的余额还剩：￥", money)
                elif chose == 5 and k == 0.1:
                    mycart.append(shop[chose])
                    print(chose)
                    money = money - k * shop[chose][1]
                    print("恭喜，成功添加购物车!,您的余额还剩：￥", money)
                elif chose == 6 and k == 0.2:
                    mycart.append(shop[chose])
                    print(chose)
                    money = money - k * shop[chose][1]
                    print("恭喜，成功添加购物车!,您的余额还剩：￥", money)
                else:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    print("恭喜，成功添加购物车!,您的余额还剩：￥", money)
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！拜拜了您嘞！")
        break
    else:
            print("对不起，输入非法，请重新输入！别瞎弄！")

#6.打印购物小票
print("以下是你的购物小票，请拿好：")
print("-------------------young商城-------------------")
print("-----------------你购买的商品如下----------------")
for key,value in enumerate(mycart):
    print(key,value)
print("你的钱包余额为：￥",money)
print("-----------------------end------------------------")



