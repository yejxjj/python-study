import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op  = list(map(int, input().split()))

maxi = -float('inf')
mini =  float('inf')

def dfs(depth, total, add, sub, mul, div):
    global maxi, mini
    if depth == N:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    
    # if depth != n인 경우 재귀 처리
    if add: 
        dfs(depth+1, total+num[depth], add-1, sub, mul, div)
    if sub:
        dfs(depth+1, total-num[depth], add, sub-1, mul, div)
    if mul:
        dfs(depth+1, total*num[depth], add, sub, mul-1, div)
    if div:
        dfs(depth+1, int(total/num[depth]), add, sub, mul, div-1)    


dfs(1, num[0], op[0],op[1],op[2],op[3])
print(maxi)
print(mini)