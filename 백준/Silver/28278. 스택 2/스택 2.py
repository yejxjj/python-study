import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
n = int(sys.stdin.readline())

# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
ss = []
for i in range(n):
    cmd = sys.stdin.readline().split()
    op = cmd[0]
   
    if (op == '1'):
        ss.append(cmd[1])

    elif (op == '2'):
        if len(ss)>0:
            print(ss.pop(-1))
        else:
            print(-1)

    elif (op == '3'):
        print(len(ss))

    elif (op == '4'):
        if len(ss)>0:
            print(0)
        else:
            print(1)

    elif (op == '5'):
        if len(ss)>0:
               print(ss[-1])
        else:
            print(-1)

