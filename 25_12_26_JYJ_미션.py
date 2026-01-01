##
##
##COUNT = 100
##START = 1.0
##END = 2.0
##
##for i in range(COUNT):
##    x = START + i*((END-START)/COUNT)
##    f = (x**2 -x -1)
##    if abs(f-0.0) < 0.01 :
##        print("방정식의 해는", x)
##
##
###조건 제어 반복-----------------------------------------
##TARGET = 2000
##money = 1000
##year = 0
##rate = 0.07
##
##while money <TARGET:
##    money = money + money * rate
##    year = year +1
##
##print(year,"년")
##
##
###예제 1과 10까지의 합 계산하기-----------------------------------------
##i = 1
##sum = 0
##
##while i<= 10 :
##    sum = sum + i
##    i = i + 1
##
##print("합계는",sum)
##
##
###else가 있는 while 루프-----------------------------------------
##i = 0
##while i < 3:
##    print("루프 안쪽")
##    i = i + 1
##else:
##    print("else 부분")
##
###무한 반복 오류-------------------------------------------------
##i = 0
##
##while i < 10 :
##    print("Hello!")
##
###Lab: 구구단 출력-------------------------------------------------
##dan = int(input("원하는 단은"))
##i = 1
##while i <= 9:
##    print("%d * %d = %d" %(dan, i, dan*i))
##    i = i +1
##
###숫자 맞추기 게임-------------------------------------------------
##import random
##
##tries = 0
##guess = 0
##answer = random.randint(1,100)
##
##print("1부터 100사이의 숫자를 맞추시오")
##
##while guess != answer:
##    guess = int(input("숫자를 입력하시오"))
##    tries = tries + 1
##    if guess < answer:
##        print("너무 낮음")
##    elif guess > answer:
##        print("너무 높음")
##
##if guess == answer:
##    print("축하합니다. 시도횟수=",tries)
##else:
##    print("정답은", answer)
###초등생을 위한 산수 문제 발생기-------------------------------------
##
##import random
##
##flag = True
##
##while flag:9
##
##    x = random.randint(1,100)
##    y = random.randint(1,100)
##    answer = int(input(f"{x} + {y} ="))
##    if answer == x + y:
##        print("잘했어요")
##    else:
##        print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?")
##        flag = False
##
##
###[실습 문제]===================================================================================
##
###1----------------------------------------------------------------
##import random
##
##
##a = ["", "가위", "바위", "보"]
##flag = True
##
##
##
##             
##while flag:
##    print("[1]가위 [2] 바위 [3] 보")
##    answer = int(input("Your choice? (1-3): "))
##    
##    com = random.randint(1,3)
##
##    print(f"컴퓨터는 [{a[com]}]를 냈습니다. 인간은 [{a[answer]}]를 냈습니다.")
##    
##    if answer == com:
##        print("결과: 비겼습니다.")
##
##    elif answer == 1:
##        if com == 2:
##                print("결과: 컴퓨터가 이겼습니다..")
##
##        else:
##                print("결과: 이겼습니다..")
##
##    elif answer == 2:
##        if com == 3:
##                print("결과: 컴퓨터가 이겼습니다..")
##        else:
##                print("결과: 이겼습니다..")
##            
##    elif answer == 3:
##        if com == 1:
##                print("결과: 컴퓨터가 이겼습니다..")
##        else:
##                print("결과: 이겼습니다..")
##
##    g = input("\n가위/바위/보 게임을 계속하시겠습니까(y/n)?")
##
##    if g == 'y': 
##        flag = True
##    else:
##        print("게임을 종료합니다.")
##        flag = False
##
###2----------------------------------------------------------------
##
##i = 1
##a = []
##while i<=100:
##    if i%3 == 0 and i%5 ==0:
##        a.append(i)
##    i = i+1
##
##print(a)
##
###3----------------------------------------------------------------
##i = 3
##a = []
##
##while i<= 70:
##    if i % 2 == 0:
##        a.append(i)
##    i  = i+1
##
##count = 0
##for num in a:
##    print(num, end=" ")
##    count = count + 1
##
##    if count % 5 == 0:
##        print()
##
##        
##
##
###4----------------------------------------------------------------
##
##
##for i in range(1,6):
##    while True:
##        length = int(input(f"막대{i}의 길이:"))
##
##        if length > 50 or length < 1:
##             print("허용범위를 벗어낫습니다. 다시 입력하세요.")
##        else:
##            print("#" * length)
##            break
##
##
##
###5---------------------------------------------------------------
##
##import turtle
##t = turtle.Turtle()
##t.shape("turtle")
##
##flag = True
##
##    
##while flag == True:
##    s = turtle.textinput("도형 정보입력", "도형을 입력하시오: ")
##    
##    if s == "사각형" :
##        t.reset()
##        w = int(turtle.textinput("사각형","가로: "))
##        h = int(turtle.textinput("사각형","세로: "))
##        for _ in range(2): 
##            t.forward(w)
##            t.left(90)
##            t.forward(h)
##            t.left(90)
##        
##    elif s == "원" :
##        t.reset()
##        r = int(turtle.textinput("원","반지름 입력: "))
##        t.circle(r)
##        
##    elif s == "정삼각형" :
##        t.reset()
##
##        side= int(turtle.textinput("정삼각","한 변의 길이: "))
##        
##        t.forward(side)
##        t.left(120)
##        t.forward(side)
##        t.left(120)
##        t.forward(side)
##        t.left(120)
##       
##
##    g = input("계속 하시겠습니까? ")
##
##    if g == 'y': 
##            flag = True
##            
##    else:
##            print("게임을 종료합니다.")
##            flag = False
##
##
##
##
