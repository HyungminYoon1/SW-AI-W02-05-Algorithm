# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque

apple_locations = set()
direction_infos = deque()
n = int(input())

# 사과 배치
for i in range(int(input())):
    r, c = map(int, input().split())
    apple_locations.add((r - 1, c - 1)) # 좌표 보정

# 방향 수정 정보 배치
for i in range(int(input())):
    t, c = input().split()
    direction_infos.append((int(t), c)) # 좌표 보정

# 방향 벡터: 기존 벡터에서 우회전은 인덱스+1, 좌회전은 인덱스-1 (mod 4)
direction_vector = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

def over_field(pos, size):
    if pos[0] < 0 or pos[0] >= size or pos[1] < 0 or pos[1] >= size:
        return True
    return False

def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def get_survival_time():

    head_location = (0, 0)
    body_locations = deque()
    snake_set = {(0, 0)} # 머리와 몸통을 모두 합친 집합(충돌 판정용)
    direction_index = 0
    t = 0

    while True:
        # 시간 추가
        t += 1

        # 새로운 헤드 위치
        next_head_location = add_tuple(head_location, direction_vector[direction_index])

        # 벽 충돌 탐지
        if over_field(next_head_location, n): # detect wall
            return t
        
        # 몸통 충돌 탐지
        if next_head_location in snake_set:
            return t
        
        # 기존의 머리는 몸통에 추가
        body_locations.append(head_location)

        # 새로운 헤드 위치를 헤드로 고정
        head_location = next_head_location
        snake_set.add(head_location)

        # 새로운 위치에 사과가 없으면 몸통 마지막 부분(꼬리) 제거
        if head_location in apple_locations:
            apple_locations.remove(head_location) # 사용한 사과 정보 제거
        else:
            tail = body_locations.popleft() # 꼬리 제거
            snake_set.remove(tail)
        
        # 새로운 방향 변화 확인
        if direction_infos and t == direction_infos[0][0]: # 방향 변경
            if direction_infos[0][1] == 'D':
                direction_index = (direction_index + 1) % 4
            elif direction_infos[0][1] == 'L':
                direction_index = (direction_index - 1) % 4
            else:
                ValueError("wrong direction code")
            direction_infos.popleft() # 사용한 방향 정보는 제거

print(get_survival_time())