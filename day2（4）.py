a=int(input("请输入你的第一条边长："))
b=int(input("请输入你的第二条边长："))
c=int(input("请输入你的第三条边长："))

if a+b>c and b+c>a and c+a>b:
    print("可以构成三角形")
    if a==b==c:
        print("等边三角形")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("等腰三角形")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("直角三角形")
    else:
        print("普通三角形")
else:
    print("不能构成三角形")