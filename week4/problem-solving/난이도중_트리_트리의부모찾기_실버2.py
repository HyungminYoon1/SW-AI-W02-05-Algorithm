# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

'''
각 노드의 부모를 구하기
'''
from collections import deque

node_count = int(input())

graph = {i:[] for i in range(1, node_count + 1)}
parent = [0 for i in range(node_count + 1)]

for _ in range(node_count-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque([1])
visited = {1}

while q:
    target = q.popleft()
    for neighbor in graph[target]:
        if neighbor not in visited:
            parent[neighbor] = target
            q.append(neighbor)
            visited.add(neighbor)

for i in range(2, node_count+1):
    print(parent[i])