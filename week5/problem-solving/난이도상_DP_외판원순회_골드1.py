# DP - 외판원 순회 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/2098

'''
풀이 전략
# 상태: dp[현재도시][방문집합]
# 현재도시에 있고, 방문집합 상태일 때 남은 도시를 모두 방문하고 출발점으로 돌아가는 최소 비용
방문 집합을 파이썬 set으로 만들면 집합이 총 2^n 개가 필요하고, dp[현재도시][방문집합] 의 크기는 n x 2^n 가 됩니다.

따라서 방문여부를 visited = 0b01011 같은 식으로 비트마스크로 저장하면 배열 인덱스로 처리하여 dp[now][visited] 와 같이 접근하여 사용 가능합니다. 
메모리 사용이 작고 연산이 매우 빠르다는 장점이 있습니다.

visited & (1 << nxt)        # 방문 여부 확인: nxt번째 비트가 1인지 확인
visited | (1 << nxt)        # 방문 처리: nxt번째 비트를 1로 만든다

보통 비트마스크의 오른쪽부터 도시 번호를 뜻합니다.
'''

## gpt가 제시한 정석 풀이

import sys
sys.setrecursionlimit(10**6)

n = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * (1 << n) for _ in range(n)] # [-1] 이라는 원소 1개짜리 리스트를 (1 << n)번 반복해서 길이가 2^n인 리스트를 만든다

now = 0 # 현재 도시: 0
visited = 1 << 0 # 최초 도시 방문 처리

INF = 10**8

# 현재 now 도시에 있고, visited에 있는 도시들을 이미 방문했을 때, 남은 도시를 모두 방문하고 0번 도시로 돌아가는 최소 비용
# 이 함수는 지금부터 앞으로 필요한 최소 비용만 계산해야 함
def dfs(now, visited):

    # 종료 조건: 모든 도시를 방문한 경우 시작점(0)으로 이동하여 복귀 비용 반환
    if visited == (1 << n) - 1:
        if cost_matrix[now][0] != 0:
            return cost_matrix[now][0]
        return INF # 시작점으로 돌아갈 수 없으면 INF 반환
    
    # 메모이제이션: 이미 계산했으면 dp 반환
    if dp[now][visited] != -1:
        return dp[now][visited]

    # 새로 계산 시작시에 dp를 INF로 초기화
    dp[now][visited] = INF

    # 다음 도시 탐색
    for nxt in range(n):
        if visited & (1 << nxt): # 방문 여부 확인: nxt번째 비트가 1인지 확인
            continue # 이미 방문한 도시 제외
        if cost_matrix[now][nxt] == 0: # 길이 없음
            continue

        # 점화식: now에 있고, visited 상태일 때, 남은 도시를 다 방문하고 0번으로 돌아가는 최소 비용
        dp[now][visited] = min(
            dp[now][visited],
            cost_matrix[now][nxt] + dfs(nxt, visited | (1 << nxt))
        )

    return dp[now][visited]

# 시작
print(dfs(now, visited))