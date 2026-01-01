
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


# 38pg: 배송비 계산 프로그램------------------------------------------

country = input("배송지(현재는 korea와 us만 가능):")
price = int(input("상품의 가격:"))

if country == "korea":
            if price >= 200000:
                    shipping_cost = 0
            else:
                    shipping_cost = 3000
else:
            if price >= 100000:
                    shipping_cost = 0
            else:
                    shipping_cost = 8000

print("배송비=", shipping_cost)
#41pg: 학점 결정 예제-----------------------------------------------------

score = int(input("성적을 입력하시오:"))

if score >= 90:
            print("학점 A")
elif score >= 80:
            print("학점 B")
elif score >= 70:
            print("학점 C")
elif score >= 60:
            print("학점 D")
else:
            print("학점 F")
##42pg: 리히터 규모-----------------------------------------------------
scale = float(input("리히터 규모를 입력하시오:"))

if scale >= 8.0:
        print("대부분의 구조물이 파괴됩니다.")
elif scale >= 7.0:
        print("지표면에 균열이 발생합니다.")
elif scale >= 4.0:
        print("빈약한 건물에 큰 피해가 있습니다.")
elif scale >= 2.0:
        print("물건들이 흔들리거나 떨어집니다.")
else:
        print("지진계에 의해서만 탐지 가능합니다.")

##44pg: 사용자 입력 검증하기-------------------------------------------
print("=============================")
print("메뉴 1번: 치즈 버거")
print("메뉴 2번: 치킨 버거")
print("메뉴 3번: 불고기 버거")
print("=============================")

selection = int(input("메뉴를 선택하세요"))

if selection >=1 and selection <=3:
        print("메뉴",selection)
else:
        print("잘못 입력하셨습니다.")

##46pg: 축구게임 ----------------------------------------------
import random

computer_choice = random.randint(1, 3)
user_choice = input("어디를 수비하시겠어요?(왼쪽: 1, 중앙: 2, 오른쪽: 3)")

if computer_choice == user_choice:
        print("수비에 성공하셨습니다. ")
else:
        print("페날티킥이 성공하였습니다. ")

##48pg: 도형 그리기 ----------------------------------------------

import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오: ")

if s == "사각형" :
    
    w = int(turtle.textinput("","가로: "))
    h = int(turtle.textinput("","세로: "))
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    
turtle.mainloop()
turtle.bye()

