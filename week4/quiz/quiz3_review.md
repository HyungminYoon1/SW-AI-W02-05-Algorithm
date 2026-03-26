# 문제

표1_3
 	
3.다음은 BFS를 구현한 코드이다. 빈칸에 들어갈 알맞은 코드를 작성하시오. 
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(__________)

# 올바른 답안
queue.extend(graph[node])

이유: 현재 방문한 node의 인접 정점들을 큐에 넣어야 BFS가 동작하기 때문입니다.