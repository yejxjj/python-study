n = int(input())
m = int(input())
s = input()

p = "I"+"OI" * n
p_num = len(p) 
count = 0

for i in range(m):
    s_part =s[i:(i+p_num)]
    if (s_part == p):
        count += 1
    
    
print(count)
