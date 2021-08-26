name = 'root'
password = 'admin'
for i in range(0,3):
    usr_name = input("用户名：")
    usr_password = input("密码：")
    if usr_name == name and usr_password == password:
        print("界面正在加载中--------")
        print("数据正在加载中--------")
        print("正在加载中--------")
        print("正在加载中--------")
        print("抱歉，系统出现故障了--------")
        break
    elif name != usr_name or password != usr_password:
        if i < 2:
            print("用户名密码错误，请重新输入！")
        else:
            print("对不起！，账户密码输入错误，已尝试登录三次，账户被锁定")


