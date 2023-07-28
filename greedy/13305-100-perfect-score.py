import sys

N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

worth = 0
key = price[0]

for i in range(N-1):
    if price[i] < key:
        key = price[i]
    worth += key * distance[i]

print(worth)

