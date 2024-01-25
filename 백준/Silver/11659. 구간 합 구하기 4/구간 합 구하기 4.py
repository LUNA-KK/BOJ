import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

# 누적 합 계산
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + num[i - 1]

for i in range(m):
    start, end = map(int, sys.stdin.readline().split())
    result = prefix_sum[end] - prefix_sum[start - 1]
    print(result)
