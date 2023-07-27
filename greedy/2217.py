import sys

N = int(sys.stdin.readline())
count = N
weight = []
weightMax = []

for _ in range(N):
    weight.append(int(sys.stdin.readline()))

weight.sort()

for _ in range(N):
    weightMax.append(weight[N-count] * count)
    count -= 1

print(max(weightMax))