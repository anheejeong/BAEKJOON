from collections import deque
import sys

A, B = map(int, sys.stdin.readline().split())
queue = deque()
queue.append((A, 1)) #시작 숫자 넣음

while(queue):
    number, counter = queue.popleft()
    # 맞는지 확인
    if number > B:
        continue
    if number == B:
        print(counter)
        break
    # 아니라면 추가
    queue.append((int(str(number) + "1"), counter + 1))
    queue.append((number * 2, counter + 1))
else:
    print(-1)