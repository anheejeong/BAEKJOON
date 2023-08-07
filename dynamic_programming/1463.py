import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]

# dp[1]은 어차피 계산 횟수에 포함되지 않으므로 0, 따라서 for문은 2부터
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])