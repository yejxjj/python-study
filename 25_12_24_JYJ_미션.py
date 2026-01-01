
#[수업 실습]---------------------------------------------------------------------
#31pg: 물의 상태 출력하기----------------------------------------------

temp = float(input("온도를 입력하시오"))

if temp <= 0 :
        print("물의 상태는 얼음입니다.\n")
    
elif temp> 0 and temp < 100:
        print("물의 상태는 액체입니다.\n")
    
else:
        print("물의 상태는 기체입니다.\n")

#32pg: 동전 던지기 게임------------------------------------------------


import random

print("동전 던지기 게임을 시작합니다.")

coin = random.randrange(2)

if coin == 0:
        print("앞면입니다.")
    
else:
        print("뒷면입니다.")

print("게임이 종료되었습니다.\n")



#34pg: 거북이 제어하기-----------------------------------------------------

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(3)
t.shapesize(3,3)

while True:
    command = input("명령을 입력하시오:")
    if command == "l":
        t.left(90)
        t.forward(100)
    if command == "r":
        t.right(90)
        t.forward(100)
    if command == "q":
            break

turtle.mainloop()
turtle.bye()

#Python 실습 과제 ========================================================================

#1----------------------------------------

temp = int(input("현재 온도는?"))

if temp >= 25:
    print("반바지 추천")
else:
    print("긴바지 추천")

#2------------------------------------------------

a = input("문자를 입력하시오")

if a == 'r' or a == 'R':
        print("사각형")
elif a == 't' or a == 'T':
        print("삼각형")
elif a == 'c' or a == 'C':
        print("원")
else:
        print("존재하지 않는 도형")

#3---------------------------------

a = int(input("분자:"))
b = int(input("분모:"))


if b > 0:
    print(float(a/b))
else:
    print("분모는 0을 사용할 수 없습니다.")
    




    
