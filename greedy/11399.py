import sys

N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
time.sort()
count = 0

for idx, val in enumerate(time):
    for i in range(0, idx):
        count += time[i]
    count += val

print(count)