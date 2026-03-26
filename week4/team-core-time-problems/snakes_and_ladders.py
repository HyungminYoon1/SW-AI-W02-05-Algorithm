
# board = [
#             [-1,-1,-1,-1,-1,-1],
#             [-1,-1,-1,-1,-1,-1],
#             [-1,-1,-1,-1,-1,-1],
#             [-1,35,-1,-1,13,-1],
#             [-1,-1,-1,-1,-1,-1],
#             [-1,15,-1,-1,-1,-1]
#         ]

from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]):
        array = board_to_1d_array(board)
        n = len(board)

        return get_minimum_pass_count(array, n)

def board_to_1d_array(board):

    n = len(board)
    array = [-1]
    start_direction_index = (n-1) % 2 # 보드의 시작 위치 홀짝 체크
    
    # 보드를 1차원 배열로 매핑
    for i in range(n):
        if (n-1-i) % 2 == start_direction_index:
            array.extend(board[n-1-i])
        else:
            array.extend(board[n-1-i][::-1])

    return array

def get_minimum_pass_count(array, n):  
    start_point_index = 1
    end_point_index = n*n
    next_index_range = [1, 2, 3, 4, 5, 6]
    
    q = deque([(start_point_index, 0)])  # 레벨 증가 포함
    visited_index = {0, 1}

    print("array == ", array)
    
    while q:
        current_index, current_level = q.popleft()
        
        for number in next_index_range:
            next_index = current_index + number
            print("current_level == ", current_level)
            
            # 순간이동 조건
            if array[next_index] != -1 and next_index not in visited_index:
                visited_index.add(next_index) # 순간이동 전 좌표 방문 처리
                next_index = array[next_index] #순간이동 이후 좌표
                q.append((next_index, current_level+1))
            
            # 단순이동 조건    
            elif next_index not in visited_index:
                visited_index.add(next_index) # 방문처리
                q.append((next_index, current_level+1))
                
            # 종료 조건
            if next_index >= end_point_index:
                return current_level + 1
    
    return -1
