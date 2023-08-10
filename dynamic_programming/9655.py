import sys

# 그냥 홀짝으로 구분해도 됨
# dp 연습 용 코드

N = int(sys.stdin.readline())
turn = [0 for _ in range(1001)]
turn[1] = 1
turn[2] = 0
turn[3] = 1

for i in range(4, N+1):
    if turn[i-1] == 1 or turn[i-3] == 1:
        turn[i] = 0
    else:
        turn[i] = 1

if turn[N] == 1:
    print('SK')
else:
    print('CY')