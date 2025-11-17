def solution(a, b):
    answer = 0
    add1= str(a)+str(b)
    add2= str(b)+str(a)
    
    if add1> add2:
        answer = int(add1)
    else: 
        answer = int(add2)
    return answer