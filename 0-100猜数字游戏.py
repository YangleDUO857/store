import random
num=random.randint(0,100)
i=0
print("--------欢迎来到猜数字游戏--------")
guessnum =int(input("请输入一个数字"))
while i < 10:
        if guessnum == num:
            print("你猜对了233")
            break
        elif guessnum < num:
            print("你猜小了233")
            i = i+1
            if i == 10:
                print("对不起，游戏结束233")
            else:
                guessnum =int(input("请输入确认的数字"))
        else:
            print("你猜大了233")
            i = i+1
            if i == 10:
                print("你猜大了233")
                i = i+1
                if i == 10:
                    print("对不起，游戏结束233")
                else:
                    guessnum =int(input("请输入确认的数字"))



