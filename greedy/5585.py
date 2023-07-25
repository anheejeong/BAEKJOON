import sys

count = 0
coin = [500, 100, 50, 10, 5, 1]

n = int(sys.stdin.readline())
n = 1000 - n

for i in coin:
    count += n // i
    n %= i

print(count)