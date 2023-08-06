import sys

N = int(sys.stdin.readline())
arr = [[0 for _ in range(0, N)] for _ in range(0, N)]

for i in range(0, N):
    for j, value in enumerate(map(int, sys.stdin.readline().split())):
        arr[i][j] = value

# Floyd-Warshall algorithm
# D[ij] = min(D[ik] + D[kj])
for k in range(0, N):
    for i in range(0, N):
        for j in range(0, N):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for i in range(0, N):
    printStr = ""
    for j in range(0, N):
        printStr += str(arr[i][j]) + " "
    print(printStr)