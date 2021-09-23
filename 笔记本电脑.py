class computer:
    __username =""
    __big =""
    __money =""
    __cpu =""
    __memory =""
    __time =""

    def setusername(self,username):
        self.__username = username

    def getusername(self):
        return self.__username

    def dazi(self,username,time,word):
        print("正在打字中",username,"已经打完了,用时",time,"打得是",word)

    def playgame(self,username,time,gamename):
        print("正在打游戏中",username,"游戏已结束,用时",time,"玩的游戏名是",gamename)

    def movie(self,username,time,moviename):
        print("正在看电影中",username,"电影已经看完了，用时",time,"看的电影名字是",moviename)

# class computer:
#     dazi = "wdnmd"
#     gamename = "王者荣耀"
#     moviename = "中国医生"
c = computer()
c.dazi("打字","1","wdnmd")
c.playgame("打游戏","15","王者荣耀")
c.movie("看电影","120","中国医生")




