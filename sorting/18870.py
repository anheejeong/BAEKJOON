import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
newArr = sorted(set(arr))

dictionary = {newArr[i] : i for i in range(len(newArr))}
for i in arr:
    print(dictionary[i], end=' ')