import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

count = 0
a = 0 
i = 1

while i < m -1:
    if s[i-1] == "I" and s[i] == "O" and s[i+1] == "I":
        count += 1

        if count == n:
            a += 1
            count -= 1
        i += 2
    else:
        count = 0
        i += 1

    
    
print(a)
