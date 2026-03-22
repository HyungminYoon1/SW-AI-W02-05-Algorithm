# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

import sys
input = sys.stdin.readline
from collections import deque

# 그래프 Bipartite Graph 인지 판별하는 함수
def is_bipartite_graph(graph, node_count):

    if not graph:
        return True

    result = True
    color_map = [-1] * (node_count + 1) # 색칠/방문처리용 매핑. 미방문은 -1 이고 2색상 칠할 때 0, 1 번갈아 배치

    def bfs(node):
        q = deque([node])
        color_map[node] = 0

        while q:
            current = q.popleft()
            for neighbor in graph[current]:
                if color_map[neighbor] == -1:
                    q.append(neighbor)
                    color_map[neighbor] = (color_map[current] + 1) % 2 # 다음 색으로 색칠하기
                elif color_map[neighbor] == color_map[current]:
                    return False # 이웃 색상이 현재 노드 색상과 같을 경우 False 반환

        return True # 해당 BFS 통과
                    
    # 분리된 그래프일 경우 추가 탐색
    for node in range(1, node_count + 1):
        if color_map[node] == -1:
            result = bfs(node)
            if not result:
                return False # 하나의 부분 그래프라도 이분그래프가 아닐 경우 False 반환

    return True # 모든 그래프에서 통과시 True 반환

k = int(input()) # k: 테스트 케이스의 개수 
graph = [[] for _ in range(k)]
result = [] # 결과를 담는 리스트

for i in range(k):
    v, e = map(int, input().split()) # v: 그래프의 정점의 개수, e: 간선의 개수
    graph = [[] for _ in range(v + 1)] # 그래프 초기화

    for _ in range(e):    
        u, t = map(int, input().split()) # 두 정점의 번호
        graph[u].append(t)
        graph[t].append(u)
    
    if is_bipartite_graph(graph, v):
        result.append("YES")
    else:
        result.append("NO")

print('\n'.join(result))