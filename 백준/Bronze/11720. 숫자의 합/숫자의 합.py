#자료구조로 해결 가능한 문제
N = int(input())
num = list(input()) #리스트에 넣기
sum = 0 

for i in num:
    sum += int(i) #형변환필요 num에는 문자형으로 들어가있음

print(sum)