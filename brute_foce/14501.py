# dynamic-programming
import sys

N = int(sys.stdin.readline())
T = []
P = []
dp = [0 for _ in range(N+1)]

for _ in range(N):
    n1, n2 = map(int, sys.stdin.readline().split())
    T.append(n1)
    P.append(n2)

for i in range(N-1, -1, -1):
    if T[i] + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[T[i] + i] + P[i])

print(dp[0])