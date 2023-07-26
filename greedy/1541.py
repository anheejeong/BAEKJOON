import sys

#line = input()
line = sys.stdin.readline().strip()
math = line.split('-')

plus = 0
minus = 0

if len(math) == 1:
    mathex = math[0].split('+')
    for k in mathex:
        plus += int(k)
else:
    for idx, val in enumerate(math):
        if(idx == 0 and val.isdigit()):
            plus += int(val)
        elif(val.isdigit()):
            minus += int(val)
        elif(idx != 0):
            mathex = val.split('+')
            for k in mathex:
                minus += int(k)
        else:
            mathex = val.split('+')
            for k in mathex:
                plus += int(k)

# 코드 정리 =>
# for i in math[0].split('+'):
#     plus += int(i)
# for i in math[1:]:
#     for j in i.split('+'):
#         plus -= int(j)

plus -= minus
print(plus)