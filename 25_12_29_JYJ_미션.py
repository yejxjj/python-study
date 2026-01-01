#과제1------------------------------------------------
height = int(input("직각 이등변 삼각형의 높이는? "))


for i in range(1, height + 1):
    for k in range(1, i + 1):
        print(k, end=" ")
    print()


#과제2------------------------------------------------
size = 5

for i in range(size):
    for j in range(size):
        if i == j or i + j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


#과제3------------------------------------------------
for i in range(1, 4):
    num = int(input(f"정수 {i} 입력:"))

    if i == 1 or num > max_val:
        max_val = num
print("\n최댓값:",max_val)


#과제4------------------------------------------------
count = 0

for num in range(2,101):
    flag = True
    for i in range(2, num):
        if num % i ==0:
            flag = False
            break
    if flag:
        print(f"{num:3}", end="")
        count += 1
        
        if count % 5 == 0:
            print()
            
     
    
    
        




