# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

from collections import deque

input() # computer_count
computer_pairs_count = int(input())

connection_list = []
not_visited = set()

for i in range(computer_pairs_count):
    t = tuple(map(int, input().split()))
    connection_list.append(t)
    not_visited.add(t)

q = deque() # 검사 대기열
infected_computers = {1}
q.append(1)

while q:
    next_target = q.popleft()
    for con in connection_list:
        if con in not_visited:
            u, v = con[0], con[1]

            if u in infected_computers and v in infected_computers:
                not_visited.remove(con)
                continue

            if next_target != u and next_target != v:
                continue

            if next_target == u:
                if v not in infected_computers:
                    infected_computers.add(v)
                    q.append(v)
                
            if next_target == v:
                if u not in infected_computers:
                    infected_computers.add(u)
                    q.append(u)

            not_visited.remove(con)

print(len(infected_computers)-1)

'''
현재 풀이의 문제점

현재 풀이에서는 connection_list 에 (u, v) 쌍을 모두 저장해 두고, 
큐에서 컴퓨터 하나를 꺼낼 때마다 연결 목록 전체를 다시 훑습니다. 
그래서 "지금 컴퓨터와 상관없는 간선"도 계속 검사하게 됩니다. 
동작은 할 수 있지만, 그래프 탐색의 핵심 구조가 직접 드러나지 않고 
not_visited 같은 보조 장치도 필요해집니다.

현재 풀이의 시간복잡도는 대략 O(V * E) 에 가깝습니다.
큐에서 컴퓨터를 하나 꺼낼 때마다 connection_list 전체를 다시 순회하기 때문입니다.
방문 가능한 컴퓨터 수가 최대 V 개이고 간선 수가 E 개이면, 최악에는 E 를 V 번 가까이 보게 됩니다.

반면 정석 풀이인 인접 리스트 BFS는 O(V + E) 입니다.
이유는 각 정점은 큐에 많아야 한 번 들어가고,
각 간선도 인접 리스트를 통해 많아야 한두 번 정도만 확인되기 때문입니다.

'''

## gpt가 제시한 정석 풀이(인접 리스트 + BFS)

from collections import deque

computer_count = int(input())
computer_pairs_count = int(input())

graph = [[] for _ in range(computer_count + 1)]

for _ in range(computer_pairs_count):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = {1}
q = deque([1])

while q:
    current = q.popleft()

    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)

print(len(visited) - 1)
