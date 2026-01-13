import sys
data = sys.stdin.read().splitlines()
    
line1 = data[0]
line2 = data[1]

def ser(line1, line2):
    cc = line1.count(line2)
    print(cc)

c = ser(line1, line2)