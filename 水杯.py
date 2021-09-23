class cup:
    __username =""
    __high =""
    __volume =""
    __color =""
    __texture =""
    __water =""

    def setusername(self, username):
        self.__username = username

    def getusername(self):
        return self.__username

    def high(self, username, high, cm):
        print("一个水杯", username, "杯子的高度是", high, "20", cm)
#vloume容积
    def vloume(self, username, volume, ml):
        print("同样的水杯", username, "杯子的容积是",volume, "500", ml)
#pure纯色
    def color(self, username, color, pure):
        print("同样的水杯", username, "杯子的颜色是", color, "blue", pure)
#textture材质
#plastics塑料
    def texture(self,username,texture,kind):
        print("同样的水杯",username,"杯子的材质是",texture,"plastics",kind)

    def water(self,username,water,any):
        print("同样的水杯",username,"杯子的作用是",water,"能存放液体",any)

# class computer:
#     high = "10"
#     vloume = "200"
#     color = "blue"
#     texture = "plastics"
#     water = "能存放液体"
c = cup()
c.high("小米","20","cm")
c.vloume("小米","500","ml")
c.color("小米","blue","纯蓝")
c.texture("小米","plastics","塑料类")
c.water("小米","保温","可食用类")


