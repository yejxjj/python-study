sel =int(input("입력진수 결정(16/10/8/2):"))

if sel !=16 and sel !=10 and sel !=8 and sel !=2 :
    print("보기의 숫자중 하나만 입력하세요")
    exit()
    
num =input("값 입력: ")

if sel ==16 :
    num1 = int(num, 16)
if sel == 10 :
    num1 = int(num,10)
if sel == 8 :
    num1 = int(num, 8)
if sel == 2 :
    num1 = int(num,2)


print("16 ==>", hex(num1))
print("10 ==>", num1)
print("8 ==>", oct(num1))
print("2 ==>", bin(num1))
