# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

# 풀이 전략
'''
dp[i][j] = i번 돌에, 마지막 점프 길이가 j일 때의 최소 점프 횟수

'''

n, m = map(int, input().split()) # n: 전체 공간, m: 착수 불가 지점 갯수
no_landing_index = set()

for _ in range(m):
    no_landing_index.add(int(input()))

# 1+2+...+k >= N이 되는 순간 그 이상 큰 점프는 사실상 필요 없음
limit = int((2 * n) ** 0.5) + 2
INF = 10**9

dp = [[INF]*(limit + 2) for _ in range(n+1)]

dp[1][0] = 0 # 초기화

for i in range(2, n+1):
    if i in no_landing_index:
        continue

    for j in range(1, limit+1):
        prev = i - j
        if prev < 1:
            break

        best = min(
            dp[i-j][j-1], # i에 j만큼 점프해서 왔다면, 직전 위치는 i-j
            dp[i-j][j],
            dp[i-j][j+1]
        ) 
        if best != INF:
            dp[i][j] = best + 1

answer = min(dp[n])
print(answer if answer != INF else -1)
