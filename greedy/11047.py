import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
count = 0

for _ in range(N):
    n = int(sys.stdin.readline())
    coin.append(n)

for i in reversed(coin):
    if K < i:
        continue
    else:
        #print(f'i : {i}')
        count += K // i
        K %= i
        #print(f'count : {count}')

print(count)

