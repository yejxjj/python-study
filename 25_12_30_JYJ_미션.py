###Lab: 피자 크기 비교
##def main() :
##    print("20cm 피자 2개의 면적:", get_area(20)+get_area(20))
##    print("30cm 피자 1개의 면적:", get_area(30))
##
##def get_area(radius) :
##    if radius > 0 :
##        area = 3.14*radius**2
##    else :
##        area = 0
##    return area
##main()

###Lab: 환영 문자열 출력 함수
##def display(msg, count=1) :
##    for k in range(count) :
##        print(msg)
##display("환영합니다.", 5)

###Lab: 주급 계산 프로그램
##def weeklyPay( rate, hour ):
##    money = 0
##    if (hour > 30):
##        money = rate*30 + 1.5*rate*(hour-30)
##    else:
##        money = rate*hour
##    return money
##
##rate = int(input("시급을 입력하시오:"))
##hour = int(input("근무 시간을 입력하시오:"))
##print("주급은 " + str(weeklyPay(rate, hour)))
#Lab: 여러 개의 값 반환
##
##def get_info():
##        name = input("이름:")
##        age = int(input("나이:"))
##        return name, age 
##st_name, st_age = get_info() 
##print("이름은 ", st_name, "이고 나이는 ", st_age, "살입니다.")
##
### Lab: 사각형을 그리는 함수 작성하기
import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(length): 
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.up()
square(100); 
t.forward(120)
square(100);
t.forward(120)
square(100);

turtle.mainloop()
turtle.bye()
#Lab: 구조화 프로그래밍 실습
##def menu() :
##    print("1. 섭씨 온도->화씨 온도")
##    print("2. 화씨 온도->섭씨 온도")
##    print("3. 종료")
##    selection = int(input("메뉴를 선택하세요: "))
##    return selection
##
##def ctof(c) : // 섭씨 -> 화씨
##    temp = c*9.0/5.0 + 32
##    return temp
##
##def ftoc(f) : //화씨 -> 섭씨
##    temp = (f-32.0)*5.0/9.0
##    return temp
##
##def input_f() :
##    f = float(input("화씨 온도를 입력하시오: "))
##    return f
##
##def input_c() :
##    c = float(input("섭씨 온도를 입력하시오: "))
##    return c
##
##def main() :
##    while True:
##        index = menu()
##    if index == 1 :
##        t = input_c()
##        t2 = ctof(t)
##        print("화씨 온도 = ", t2, "\n")
##    elif index == 2 :
##        t = input_f()
##        t2 = ftoc(t)
##        print("섭씨 온도 = ", t2, "\n")
##    else :
##        break
##main()

# Lab: 함수 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)

def f(x):
    return x**2+1

t.goto(200, 0)
t.goto(0, 0)
t.goto(0, 200)
t.goto(0, 0)

for x in range(150):
        t.goto(x, int(0.01*f(x)))
        
turtle.mainloop()
turtle.bye()
