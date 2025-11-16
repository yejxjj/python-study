# 입력문자를 거꾸로 출력하기
inStr =''

if __name__ == "__main__" :
    inStr = input('문자열 입력')

    for i in range(len(inStr)-1,-1,-1):
        print('%c' % inStr[i], end='')