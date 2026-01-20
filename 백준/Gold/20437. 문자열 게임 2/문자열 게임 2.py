import sys

input = sys.stdin.readline

t = int(input())
j = 0

while j < t:
    w = input().strip()
    k = int(input())

    char = {}
    sal  = {}

    for idx, key in enumerate(w):
        if key not in char:
            char[key] = []
        char[key].append(idx)
        
        if len(char[key]) >= k:
            sal[key] = char[key]

    if not sal:
        print(-1)

    else:
        miin = 10001
        maax = 0
        for key in sal:
            for m in range (len(sal[key]) - k + 1): 
                temp = []
                temp = sal[key][m:m+k]
                
                fst_val = temp[0]
                lst_val = temp[-1]
                
                num = lst_val - fst_val + 1

                if num >= maax:
                   maax = num
                   
                if num <= miin:
                     miin = num
                
                        
        print(miin, maax)

    j += 1   
