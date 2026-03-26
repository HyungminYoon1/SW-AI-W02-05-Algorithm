
class Solution:
    def numIslands(self, grid: List[List[str]]):
        return get_land_count(grid)

from collections import deque

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def get_land_count(grid):
    m = len(grid)
    n = len(grid[0])

    # 그래프 초기화
    graph = {}
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                graph[(i, j)] = []

    # 방향 벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 그래프의 각 좌표 간 연결관계 매핑
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                        graph[(i, j)].append((ni, nj))

    land_count = 0
    visited = set()
    
    for element in graph:
        if element in visited:
            continue

        visited.add(element)
        q = deque([element])

        while q:
            current = q.popleft()

            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        land_count += 1

    print(land_count)

get_land_count(grid)