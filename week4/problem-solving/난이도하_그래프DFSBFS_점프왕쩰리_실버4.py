# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

'''
풀이 전략
오른쪽으로 움직이는 함수
아래로 움직이는 함수
각각 이전 단계에서 도달한 마지막 위치에서 값을 받아 우방향, 하방향으로 재귀 탐색. 

성공조건: 좌표 n,n 에 도달 (또는 노드의 값이 -1)
'''

'''

# 풀이1: DFS 활용

board = []
n = int(input()) # 보드 사이즈

# 보드 초기화
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)

# 풀이1: 재귀 활용
def attend_destination_from(x, y):
    
    # 종료조건
    if x == n and y == n:
        return True
    if x > n or y > n:
        return False

    val = board[x-1][y-1]
    if val == -1:
        return True
    if val == 0:
        return False

    down, right = False, False
    
    # 재귀 탐색
    if x + val <= n:
        down = attend_destination_from(x + val, y) # 하방향
    if y + val <= n:
        right = attend_destination_from(x, y + val) # 우방향
    
    return down or right

print("HaruHaru" if attend_destination_from(1, 1) else "Hing")
'''

# 풀이2: BFS 활용

from collections import deque

board = []
n = int(input()) # 보드 사이즈

# 보드 초기화
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)

def get_all_reachable_points_from(first_point):
    q = deque([first_point])
    visited = {first_point}
    reachable_points = [first_point]

    while q:
        x, y = q.popleft()

        def get_val(x, y):
            if x < 1 or x > n or y < 1 or y > n:
                return None
            return board[x-1][y-1]
        
        val = get_val(x, y)

        next_point_down = (x + val, y)
        next_val_down = get_val(next_point_down[0], next_point_down[1])
        if next_point_down not in visited and next_val_down is not None and next_val_down != 0:
            q.append(next_point_down)
            reachable_points.append(next_point_down)

        next_point_right = (x, y + val)
        next_val_right = get_val(next_point_right[0], next_point_right[1])
        if next_point_right not in visited and next_val_right is not None and next_val_right != 0:
            q.append(next_point_right)
            visited.add(next_point_right)
            reachable_points.append(next_point_right)

    return reachable_points

first_point = (1, 1)
destination_point = (n, n)
reachable_points = get_all_reachable_points_from(first_point)

print("HaruHaru" if destination_point in reachable_points else "Hing")
