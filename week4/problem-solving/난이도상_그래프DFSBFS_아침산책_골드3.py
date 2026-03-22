# 그래프, DFS, BFS - 아침 산책 (백준 골드3)
# 문제 링크: https://www.acmicpc.net/problem/21606

'''
풀이 전략
# 시작 및 종료 노드 후보 검토: is_indoor[i] == True 이어야 함.
# 중간 노드 후보 검토: is_indoor[i] == False 이어야 함.
# 지나왔던 노드는 다시 가지 않기
'''

from collections import deque

n = int(input())
is_indoor = [False] * (n+1)
tree_graph = [[] for i in range(n+1)]

indoor = list(map(int, input().strip()))
for i in range(n):
    if indoor[i] == 1:
        is_indoor[i+1] = True 

for _ in range(n-1):
    u, v = map(int, input().split())
    tree_graph[u].append(v)
    tree_graph[v].append(u)

outside_nodes = []
inside_nodes = []

for i in range(1, n+1):
    if is_indoor[i]:
        inside_nodes.append(i)
    else:
        outside_nodes.append(i)

walking_route = set() # 가능한 산책 경로(튜플로 저장)

def dfs(node, current_route, visited_nodes):

    for next_node in tree_graph[node]:
        if next_node not in visited_nodes:
            visited_nodes.add(next_node)
            current_route = current_route + (next_node,)
            
            if is_indoor[next_node]: # 산책 종료 조건
                walking_route.add(current_route) 
            else:
                dfs(next_node, current_route, visited_nodes)
            
for start_node in inside_nodes:
    dfs(start_node, (start_node,), {start_node})
    
print(len(walking_route))

'''
현재 코드의 문제점
- 시간 복잡도가 높고 최악에 가까운 경우 거의 O(n^2) 수준까지 커져 시간 초과 위험이 큽니다.

이 문제는 보통 “실외 연결요소마다 인접 실내 수를 세어 조합 계산”으로 풀어야 합니다.
'''

## gpt가 제안한 개선 코드

from collections import deque

n = int(input())
indoor_str = input().strip()
is_indoor = [False] + [c == '1' for c in indoor_str]
graph = [[] for _ in range(n + 1)]

answer = 0 # 산책 경로

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    # 실내 - 실내 다이렉트로 연결시에도 산책경로로 처리
    if is_indoor[a] and is_indoor[b]:
        answer += 2 # 정방향, 역방향

# 실외 연결요소 탐색
visited = [False] * (n + 1)

for node in range(1, n + 1):
    if is_indoor[node] or visited[node]:
        continue

    q = deque([node])
    visited[node] = True
    indoor_count = 0 # 현재 탐색 중인 하나의 실외 연결요소에 인접해 있는 실내 정점의 개수

    while q:
        current = q.popleft()

        for nxt in graph[current]:
            if is_indoor[nxt]:
                indoor_count += 1
            elif not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

    answer += indoor_count * (indoor_count - 1)

print(answer)