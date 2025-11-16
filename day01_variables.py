# print()
print("100")
print("%d", "%d" % 100, 200)
print("100 + 100")
print("%d" %(100+100))
print("%d %d" % (100,100))

# %d, %x, %o (정수 10,16,8진수)
# %f(실수)
# %c(한글자)
# %s(두 글자 이상 문자열)

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가\"강조\"되는 효과1")
print("글자가\'강조\'되는 효과\\")
# --------------------------------------------------------------
# 변수
# 파이썬은 다른 언어와 달리 변수를 선언하지 않아도 됨
#type()함수로 변수의 자료형 확인가능
boolVar = True
animal= "동물"
height=34
height2=43.44
print(type(boolVar),type(animal),type(height),type(height2))
#변수에 값을 담으면 기존 값은 없어지고 새로운 값으로 변경됨
myVar =100
print(type(myVar))
myVar=130.33
print(type(myVar))
