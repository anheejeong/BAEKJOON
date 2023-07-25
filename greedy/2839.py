import sys

N = int(sys.stdin.readline())
count = 0

while(N % 5 != 0 and N > 0):
    count += 1
    N -= 3
if(N % 5 == 0):
    count += N // 5
elif(N != 0):
    count = -1

print(count)
