def solution(ineq, eq, n, m):
    if eq == "!":
        answer = (n < m) if ineq == "<" else (n > m)
    else: 
        answer = (n <= m) if ineq == "<" else (n >= m)
    return int(answer)