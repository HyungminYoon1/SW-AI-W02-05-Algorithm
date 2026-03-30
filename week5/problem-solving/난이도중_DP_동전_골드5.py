# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

def get_pay_method_count(coin_list, total_value):

    dp = {} # '(인덱스, 잔여금액) : 가치 ' 조합이 키와 값으로 들어감

    def dfs(idx, remaining):
        # 목표 금액을 정확히 만들었으면 1가지
        if remaining == 0:
            return 1
        
        # 동전을 다 썼는데도 금액이 남아있으면 0가지
        if idx == len(coin_list):
            return 0
        
        key = (idx, remaining)
        if key in dp:
            return dp[key]

        coin = coin_list[idx]
        count = 0
        max_count = remaining // coin

        for i in range(max_count + 1):
            next_remaining = remaining - i * coin
            count += dfs(idx + 1, next_remaining)

        dp[key] = count
        return count

    return dfs(0, total_value)

t = int(input())
result_list = []

for i in range(t): # 테스트 케이스 숫자
    n = int(input()) # 동전의 가지수
    
    # 동전 리스트 초기화
    coins = sorted(map(int, input().split()), reverse=True) # 큰 동전부터 배치해야 연산이 효율적
    total_value = int(input())

    result = get_pay_method_count(coins, total_value)
    result_list.append(result)

for result in result_list:
    print(result)


## gpt가 제시한 정석 풀이
'''
핵심 아이디어는:

dp[x] = 금액 x를 만드는 경우의 수
처음에는 dp[0] = 1
각 동전을 하나씩 보면서, 그 동전을 사용할 수 있는 금액들을 누적 갱신

dp[value - coin]에 현재 동전을 붙이면 value를 만드는 방법이 됩니다.
동전을 바깥 반복문에 두기 때문에 순서만 다른 중복 조합을 세지 않습니다.
시간 복잡도는 O(n * m)이라서 매우 안정적입니다.

'''

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1 # 0원을 만드는 방법은 아무 동전도 쓰지 않는 1가지

    for coin in coins: # 동전을 바깥 루프에서 종류별로 하나씩 순차적으로 처리하므로 조합만 세고 순열은 세지 않습니다. 따라서 같은 조합이 순서만 바뀌어 여러 번 카운팅되지 않습니다.
        for value in range(coin, m + 1):
            dp[value] += dp[value - coin] # 현재 동전 coin을 하나 쓰면 나머지 value - coin원을 만드는 방법 수만큼 새로운 경우가 생긴다

    results.append(dp[m])

for result in results:
    print(result)

