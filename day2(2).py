n=0
for i in range(0,10):
    print("请输入数字：")
    a = int(input())
    n += a
print("输入数字的和为：",n)

n=0
for i in range(0,10):
    print("请输入数字：")
    a = int(input())
    if a>n:
        n=a
print("输入的数字最大为：",n)

n=0
for i in range(0,10):
    print("请输入数字：")
    a = int(input())
    n=n+a
print("输入的数字的平均数为：",n/10)


