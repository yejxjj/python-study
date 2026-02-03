
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

ans = [-1] * N
stk = [] #아직 오큰수를 못만난 애들을 위한 정류장, 값이 아닌 인덱스를 넣어줌

for i in range(N):
    while stk and lst[stk[-1]]<lst[i]:
        idx = stk.pop()
        ans[idx] = lst[i]
    stk.append(i)

print(*ans)