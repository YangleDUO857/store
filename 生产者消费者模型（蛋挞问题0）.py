from threading import Thread
import threading
import time

danta = 500
a = threading.RLock()   #线程锁

class cook(Thread):
    count = 0
    username = ""

    def run(self) -> None:
        global danta
        end = 0
        while True:
            if danta < 498 :
                end = 0
                a.acquire()  # 打开线程锁
                self.count = self.count + 1
                danta = danta + 1
                print("还有",danta,"个蛋挞")
                time.sleep(0.01)
                a.release()     #关闭线程锁
            elif danta >=500 :
                end = end + 1
                time.sleep(2)

            if end == 2 :
                break
            # else:
            #     print(self.username,"共做了",self.count,"个蛋挞")
            #     break

class person(Thread):
    count = 0
    money = 3000
    user = ""

    def run(self) -> None:
        global danta
        while True:
            if self.money > 0 and danta > 0:
                a.acquire()
                self.money = self.money - 20
                self.count = self.count + 1
                danta = danta - 1
                print(self.user,"抢到了蛋挞","余额",self.money)
                time.sleep(0.01)
                a.release()
            elif self.money ==0:
                print(self.user,"没有钱了")
                print(self.user,"抢到了",self.count,"个蛋挞")
                exit()
            elif danta == 0 :
                time.sleep(3)


c1 = cook()
c2 = cook()
c3 = cook()
c1.username = "赵大厨"
c2.username = "钱大厨"
c3.username = "孙大厨"

p1 = person()
p2 = person()
p3 = person()
p4 = person()
p5 = person()
p6 = person()
p1.user = "熊大"
p2.user = "熊二"
p3.user = "皮皮"
p4.user = "吉吉国王"
p5.user = "小飞"
p6.user = "光头强"

c1.start()
c2.start()
c3.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()