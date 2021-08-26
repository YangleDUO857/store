import random
n = 0
sum = 0
while n < 10:
    num = random.randint(1,100)
    sum = sum + num
    n += 1
    print(num, end=",")
print()
print("10个数的和为：%d" % sum)