import sys
from collections import deque

N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split())) #N
price = list(map(int, sys.stdin.readline().split())) #N+1

# list.index(x) => list에서 x의 위치(index) find
rank = [sorted(price).index(i)+1 for i in price]

queue = deque()
queue.append((distance[0], price[0], rank[0]))
key = rank[0]
keypr = price[0]
count = 0
worth = 0

while(queue):
    dis, pri, rn = queue.popleft()
    if rn < key:
        key = rn
        keypr = pri
        worth += keypr * dis
    else:
        worth += keypr * dis
    count += 1
    if count == N-1:
        break
    queue.append((distance[count], price[count], rank[count]))

print(worth)