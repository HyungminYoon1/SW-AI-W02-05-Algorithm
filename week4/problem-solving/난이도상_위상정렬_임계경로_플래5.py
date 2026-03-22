# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948

'''
풀이 전략
위상정렬, 최장 경로 DP
역추적/역방향 그래프
'''

from collections import deque

n = int(input()) # 노드의 갯수
m = int(input()) # 간선의 갯수

graph = [[] for _ in range(n+1)] # 그래프 초기화
reverse_graph = [[] for _ in range(n+1)] # 역방향 그래프 초기화
in_degree = [0]*(n+1) # 진입차수 초기화
dist = [0]*(n+1) # 시작 도시에서 각 도시까지 도달하는 데 걸리는 최대 시간(동적 계획으로 할당)

for i in range(m):
    u, v, w = map(int, input().split()) # u -> v 노드로 이동하는데 w 시간 소요
    graph[u].append((v, w))
    reverse_graph[v].append((u, w))
    in_degree[v] += 1

start, destination = map(int, input().split()) # 시작, 끝 노드 번호

q = deque([start]) # 정방향 작업큐

while q:
    current_node = q.popleft()

    for neighbor in graph[current_node]:
        (next_node, next_time) = neighbor

        dist[next_node] = max(dist[next_node], dist[current_node] + next_time) # 최장시간 계산
        in_degree[next_node] -= 1

        if in_degree[next_node] == 0:
            q.append(next_node)

result_1 = dist[destination]

q2 = deque([destination]) # 역방향 작업큐
visited = [False] * (n+1)
visited[destination] = True
max_route_count = 0

while q2:
    current_node = q2.popleft()

    for neighbor in reverse_graph[current_node]:
        (prev_node, prev_time) = neighbor
        if dist[prev_node] + prev_time == dist[current_node]:
            max_route_count += 1
            if not visited[prev_node]:
                q2.append(prev_node)
                visited[prev_node] = True

print(result_1)
print(max_route_count)