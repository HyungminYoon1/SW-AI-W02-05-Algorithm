# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

'''
풀이 전략
어떤 작업의 시작 시각 = 선행작업들의 종료 시각 중 최댓값
어떤 작업의 종료 시각 = 그 시작 시각 + 자기 작업 시간

'''

from collections import deque

n = int(input()) # 노드의 갯수

# 그래프 초기화
graph = {i:[] for i in range(1, n + 1)}
in_degree = [0] * (n + 1)
work_time = [0] * (n + 1) # 각 노드별 작업시간
dp = [0] * (n + 1) # (선행 작업을 모두 고려한 뒤) i번 작업의 최소 완료 시간

for i in range(1, n+1):
    line = list(map(int, input().split()))
    work_time[i] = line[0]
    count = line[1]

    for j in range(count):
        prev = line[2 + j]
        graph[prev].append(i) # 그래프 노드에 간선 매핑
        in_degree[i] += 1

q = deque()

# 큐에 in_degree = 0 인 노드 추가
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append(i)
        dp[i] = work_time[i]

while q:
    current = q.popleft()
    
    # nxt: 다음 후보들
    for nxt in graph[current]:
        dp[nxt] = max(dp[nxt], dp[current] + work_time[nxt])
        in_degree[nxt] -= 1    

        if in_degree[nxt] == 0:
            q.append(nxt)

print(max(dp))