import sys

N = int(sys.stdin.readline())
meeting = []

for _ in range(N):
    n1, n2 = map(int, sys.stdin.readline().split())
    meeting.append([n1, n2])

# lambda 표현식 => 바로 정의하여 사용하는 함수
# key를 사용해서 정렬 => key 인자에 함수를 넘겨주면 우선 순위가 정해짐
# key = lambda x: (x[1], x[0]) 인 경우 => x[1]이 우선 순위가 높고 그 다음 x[0]
meeting.sort(key = lambda x: (x[1], x[0]))

count = 1
endTime = meeting[0][1]
for i in range(1, N):
    if endTime <= meeting[i][0]:
        count += 1
        endTime = meeting[i][1]

print(count)