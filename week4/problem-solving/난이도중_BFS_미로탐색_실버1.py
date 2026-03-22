# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int, input().split()) # n: 행, m: 열

# 보드 초기화
board = []
for i in range(n):
    line = list(map(int, input().strip()))
    board.append(line)

# 최단 거리 동적 계획법 초기화
board_dp_distant_map = [[0] * m for _ in range(n)]
board_dp_distant_map[0][0] = 1 # 시작 위치

def bfs():
    start_pos = (0, 0)
    end_pos = (n-1, m-1)
    
    visited = {start_pos}
    q = deque([start_pos])
    step_count = 0

    def get_accesible_neighbors(pos_x, pos_y):

        neighbors = []
        
        vectors = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
        for vec in vectors:
            new_pos_x = pos_x + vec[0]
            new_pos_y = pos_y + vec[1]

            if 0 > new_pos_x or new_pos_x >= n or 0 > new_pos_y or new_pos_y >= m:
                continue
            elif board[new_pos_x][new_pos_y] == 1:
                neighbors.append((new_pos_x, new_pos_y))
            
        return neighbors

    while q:
        current = q.popleft()
        x, y = current
        step_count += 1
        board_dp_distant_map[x][y] = min(board_dp_distant_map[x][y], step_count)
        
        for next_pos in get_accesible_neighbors(x, y):
            if next_pos not in visited:
                nx, ny = next_pos
                q.append(next_pos)
                visited.add(next_pos)
                board_dp_distant_map[nx][ny] = board_dp_distant_map[x][y]+1
        
        if current == end_pos:
            return board_dp_distant_map[n-1][m-1]
    
    return None

print(bfs())
