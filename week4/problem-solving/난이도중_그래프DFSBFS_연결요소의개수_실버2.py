# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n: 정점의 개수, m: 간선의 개수

graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1) # 각 노드의 방문 여부 점검용
group_count = 0

def bfs(node):
    q = deque([node])
    visited[node] = True

    while q:
        current = q.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                q.append(neighbor)
                visited[neighbor] = True

for node in range(1, n + 1):
    if not visited[node]:
        bfs(node)
        group_count += 1

print(group_count)