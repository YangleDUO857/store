#
# 中国工商银行开发
#1.编程实现：仔细业务的包含关系，并完成以下编程需求，要适当提高代码的可性。
# a)：账号（str：系统随机产生8位数字）、姓名（str）、密码（int:6位数字）、地址、矿资源（int）、户行（银行的名称（str））
# b)地址：国家(str)、重点地址(str)、街道(str)、门牌号(str)
#c) 银行能存100个用户的库（可用银行，可用）、本名称（例如：中国工商银行的昌平支行，str）
#环保银行业务功能
# 1. 添加用户（参数参数：用户的所有信息。返回值：整型值（1：成功，2：用户已存在，3：用户库已满））
# a) 业务逻辑：
#  先检查该用户的账号在库里是否存在。如果不存在则在用户库里添加一个该用户并返回代号1
#  如果存在则返回代号2。另外在添加用户的时候检测用户库是否已注册满，若已则返回代号3
#2.存钱（价值值：用户的账户、访问的金额。返回值：布尔类型值）
# a) 业务逻辑：
#  先根据如果的账户信息查询用户库里是否有该用户。
#  若有，则用户的金额存入。
# 3. 取钱（价值：用户的账号，密码，取钱的数量。返回值：整型值（0：正常用户：账号不存在，2：密码不对，3：钱币）
# a) 业务逻辑：
#  先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
#  若存在，则继续判断密码是否正确，若不正确，则返回代号2。
#若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
#  若满足，则用户的关注度。
# 4. 转账（秘值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：地址不对，2密码不对，3钱密码）
# a) 业务逻辑：
#  先查询用户库是否转出和转入的账户存在，若不存在则返回代号，1，
#  若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
#  若正确则继续判断要转出的金额是否为宜，若真理则返回3，
#  否则正常转出，转出的账户用户金额要相对应的减少，转入的金额相对应的。
# 5. 账户查询功能（最高值：账号，账号，返回值：空）
# a) 业务逻辑：
#  先根据账号判断用户库是否存在该用户，如果不存在则打印提示信息：该用户不存在。
#  否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
#  若账户和密码都正确，则用户的信息都打印出来，例如：当前账号：xxxx，密码：xxxxxx，余额：xxxx元，用户居住地址：xxxxxxxxxxxx，当前账户的户开行：xxxxxxx。
# d) 界面类：在执行该入口程序时，就打印银行业务选择菜单： 例如：
#二。然后就开始处理各种输入操作，直到业务处理完成！
# 答案：
#
#开户
import random
bank={}
bank_name='环保银行'

def kaihu():
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    address=input('请输入您的地址')
    money=0
    if len(bank)>=100:
        print('对不起(＞人＜；)，实注册用户名额已满')
    elif username in bank:
        print('该用户名已注册')
    else:
        bank[username] = {
            # "account": account,  #
            "password": password,
            'address':address,
            # "country": country,
            # "province": province,
            # "street": street,
            # "door": door,
            "money": 0,
            "bank_name": bank_name
        }
        info='''
                ----------个人信息---------
                       用户名:%s        
                       密码：*****       
                       地址：%s          
                       余额：%s          
                       开户行名称：%s     
                --------------------------
                开户成功
        '''
        print(info%(username,bank[username]['address'],bank[username]['money'],bank_name))
def cunqian():
    while True:
        username=input('请输入用户名:')
        password=input('请输入密码：')
        if username not in bank:
            print('对不起(＞人＜；)，系统检测您未开户，请先开户')
            break
        else:
            while bank[username]['password']!=password:
                password=input("密码错误,请重新输入密码")
            print('您现在账户%s元' % (bank[username]['money']))
            a=input('请输入存款金额：')
            if a.isdigit():
                bank[username]['money']+=int(a)
                print('尊敬的客户·,存钱已完成，您现在账户余额为：%s'%(bank[username]['money']))
                break
            else:
                print('请输入正确的信息，笨蛋~~')
                
def quqian():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        if username not in bank:
            print('对不起(＞人＜；)，系统检测您未开户，请先开户')
            break
        else:
            while bank[username]['password'] != password:
                password = input("密码错误,请重新输入密码")

            print('您现在账户%s元'%(bank[username]['money']))
            a=input('请输入取款金额：')
            if a.isdigit():
                if int(a)<= bank[username]['money']:
                    bank[username]['money']-=int(a)
                    print('尊敬的%s,取款已完成，您现在账户余额为：%s'%(username,bank[username]['money']))
                    break
                else :
                    print("what fuck you baby forever??!!")
            else:
                 print('请输入正确的信息，笨蛋~~')


# 定义转账方法
def zhuanzhang():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        if username not in bank:
            print('对不起(＞人＜；)，系统检测您未开户，请先开户')
            break
        else:
            while bank[username]['password'] != password:
                password = input("密码错误,请重新输入密码")

            shoukuanname=input('请输入要转给的用户名：')
            while shoukuanname not in bank:
                shoukuanname=input('你要转账的用户不存在，请重新输入：')
            if username==shoukuanname:
                print("what fuck you baby forever?？!!")
                continue
            print('您现在账户%s元' % (bank[username]['money']))
            gomoney=input('请输入转账金额')
            if gomoney.isdigit():
                if int(gomoney)<= bank[username]['money']:
                    bank[username]['money']-=int(gomoney)
                    bank[shoukuanname]['money'] += int(gomoney)
                    print('尊敬的%s,转账已完成，您现在账户余额：%s'%(username,bank[username]['money']))
                    break
                else :
                    print("what fuck you baby forever??!!")
            else:
                 print('请输入正确的信息，笨蛋~~')
def chaxun():
    while True:
        username = input('请输入用户名:')
        password = input('请输入密码：')
        while username not in bank:
            username=input('你所查询的用户不存在，请重新输入要查询的用户')

        while bank[username]['password'] != password:
            password = input("密码有误,请重新输入密码")
        info = '''
                ----------个人信息---------
                       用户名:%s        
                       密码：*****       
                       地址：%s          
                       余额：%s          
                       开户行名称：%s     
                --------------------------
                '''
        print(info % (username, bank[username]['address'], bank[username]['money'], bank_name))

while True:
    print('''
    --------------欢迎来到环保银行---------------
    -------------------------------------------
    ----------1.开户            ----------------
    ----------2.存钱            ----------------
    ----------3.取钱            ----------------
    ----------4.转账            ----------------
    ----------5.查询            ----------------
    ----------6.退出           -----------------
    -------------------------------------------
    -------------------------------------------
    ''')
    chose = input('你好，我是你的语音助手摩西，请输入操作项')
    if chose=='1':
        kaihu()
    elif chose=='2':
        cunqian()
    elif chose=='3':
        quqian()
    elif chose=='4':
        zhuanzhang()
    elif chose=='5':
        chaxun()
    else:
        print('欢迎下次使用，再见！')
        break