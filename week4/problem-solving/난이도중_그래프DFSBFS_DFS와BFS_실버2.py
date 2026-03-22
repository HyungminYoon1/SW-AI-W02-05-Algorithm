# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

from collections import deque

# n: 정점의 개수, m: 간선의 개수, v: 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())

# 그래프 초기화
graph = {i:[] for i in range(1, n+1)}

# 그래프 매핑(양방향)
for i in range(m):
    u, t = map(int, input().split())
    graph[u].append(t)
    graph[t].append(u)

for node in graph:
    graph[node].sort()

# dfs
def dfs(graph, start, visited=None):

    if visited is None:
        visited = []

    visited.append(start)

    for next_node in graph.get(start, []):
        if next_node not in visited:
            dfs(graph, next_node, visited=visited)

    return visited

# bfs
def print_bfs(init_node):
    if init_node == None:
        return ""
    
    result_list = []
    q = deque([init_node])
    visited = {init_node}

    while q:
        current = q.popleft()
        result_list.append(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
    
    print(*result_list)

print(*dfs(graph, v, visited=None))
print_bfs(v)
