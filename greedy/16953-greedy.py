import sys

A, B = map(int, sys.stdin.readline().split())
count = 1
check = 0

# 끝자리가 1 제외 홀수는 나올 수 없음
while(B != A):
    count += 1
    temp = B
    if B % 10 == 1: #끝자리가 1일때
        B //= 10 #끝자리 1 빼기
    elif B % 2 == 0: #짝수일 때
        B //= 2

    if temp == B:
        check = -1
        break

if check == -1:
    print(-1)
else:
    print(count)