jing=-20
up=3
down=-2
num=1
while jing<0:
 print ('day ',num,end="   ")
 jing+=up
 print('up',jing,end="   ")
 if jing>=0:
  break
 jing+=down
 print('down',jing)
 if jing>=0:
 print("恭喜你，爬出来了")
  break

