# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

'''
배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력
(가정) 무게의 단위는 1이고, 각각의 무게는 1 이상의 자연수만 존재

1차원 배열 표준 풀이 전략
# 상태정의: dp[w] = 현재까지 고려한 물건들로, 배낭 허용 무게가 w일 때 얻을 수 있는 최대 가치
# 점화식: dp[w] = max(dp[w], dp[w - weight] + value) ## 현재 물건의 무게 weight, 가치 value
# 초기값: dp = [0] * (k + 1)
# 순회순서: 물건을 하나씩 보면서, 무게는 큰 쪽에서 작은 쪽으로 순회
# 정답위치: dp[k]

2차원 배열 표준 풀이 전략
# 상태정의: dp[i][w] = 앞의 i개 물건으로 무게 w 이하에서 얻는 최대 가치
# 점화식: 안고르면 dp[i-1][w], 고르면 dp[i-1][w-weight[i]] + value[i]
# 초기값: dp[0][w] = 0
# 순회순서: 물건을 하나씩 늘리며, 1차원 최적화시 0/1 배낭은 무게 역순
# 정답위치: dp[n][capacity]
'''

n, weight_limit_k = map(int, input().split())

item_list = []

# 방어코드
if n < 1:
    print(0)
    exit()

for _ in range(n):
    weight, value = map(int, input().split())

    if weight > 0 and value > 0:
        item_list.append((weight, value))

dp = [0] * (weight_limit_k + 1)

for w, v in item_list:
    for capacity in range(weight_limit_k, w - 1, -1):
        # dp[c] = 현재까지 물건들로 무게 한도 c에서 만들 수 있는 최대 가치
        dp[capacity] = max(dp[capacity], dp[capacity - w] + v) # dp[c] = max(안 넣기, 넣기)

print(dp[weight_limit_k]) # 배낭 최대 허용 무게가 k일 때 얻을 수 있는 최대 가치
