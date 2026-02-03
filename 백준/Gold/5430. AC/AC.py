import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    raw_arr = input().strip()[1:-1]
    
    if n == 0:
        queue = deque()
    else:
        queue = deque(raw_arr.split(','))

    flag = 0  
    is_error = False

    for cmd in p:
        if cmd == 'R':
            flag += 1
        elif cmd == 'D':
            if not queue:
                print("error")
                is_error = True
                break
            else:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    
    if not is_error:
        if flag % 2 != 0:
            queue.reverse()
        
        print("[" + ",".join(queue) + "]")