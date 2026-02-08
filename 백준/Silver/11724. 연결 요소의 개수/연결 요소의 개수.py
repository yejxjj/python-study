import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)] #인접 리스트 초기화
visited = [False] * (n+1) #방문 리스트 초기화

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


# 인접 리스트에 값 넣기
for i in range(m):
    s, e = map(int, input().split())
    #양뱡향으로 넣어줌
    A[s].append(e)
    A[e].append(s)

count = 0 #연결 요소 개수 카운팅

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)
    
print(count)