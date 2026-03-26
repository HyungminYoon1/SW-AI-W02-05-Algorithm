# 문제

4. DFS를 재귀가 아닌 스택을 이용해 구현하였다. 빈칸을 채워 코드를 완성하시오. 
graph = { 1: [2, 3], 2: [4], 3: [], 4: [] }
start = 1
visited = set()
stack = [start]
while stack:
    node = stack.pop()
    if node not in visited:
        visited.add(node)
        ________________________________________

# 올바른 답안
stack.extend(graph[node]) # DFS 자체는 동작
또는
stack.extend(reversed(graph[node])) # 인접 리스트에 적힌 순서대로 방문시키고 싶을 경우
