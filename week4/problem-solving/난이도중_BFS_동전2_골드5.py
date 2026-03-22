# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

'''
BFS 풀이 전략

1) 현재 금액을 하나의 상태로 본다.
2) 동전 하나를 추가하면 다음 금액으로 이동한다.
3) BFS는 "이동 횟수가 적은 것부터" 탐색하므로,
4) 처음 k에 도달했을 때가 최소 동전 개수다.

'''
from collections import deque

n, k = map(int, input().split()) # n: 동전 종류, k: 가치의 합
currency_unit = []

for i in range(n):
    currency_unit.append(int(input()))

currency_unit.sort()

def bfs():

    coin_count = 0
    q = deque([(0, 0)]) # (현재 누적금액, 누적 사용 동전수) = (0, 0)
    visited = [False] * (k + 1)
    visited[0] = True # 누적금액별 방문 여부 체크

    while q:
        (current_money_sum, coin_count) = q.popleft()
        
        for next_coin in currency_unit:
            next_money_sum = current_money_sum + next_coin

            if next_money_sum == k:
                return coin_count + 1

            if next_money_sum < k and not visited[next_money_sum]: # 다음 금액을 만듦
                visited[next_money_sum] = True
                q.append((next_money_sum, coin_count + 1))
    
    return -1

print(bfs())
