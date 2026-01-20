import sys

input = sys.stdin.readline

t = int(input())
j = 0

while j < t:
    w = input().strip()
    k = int(input())

    char = [[]for _ in range(26)]

    for idx, key in enumerate(w):
        code = ord(key) - ord('a')
        char[code].append(idx)
        
    result = []
    for key in char:
        if len(key) < k:
             continue
        
        for m in range (len(key) - k + 1): 
            
                val = key[m+k-1] - key[m] + 1

                result.append(val)
    if not result:
        print(-1)
    else:   
        print(f"{min(result)} {max(result)}")
    j += 1   

    
