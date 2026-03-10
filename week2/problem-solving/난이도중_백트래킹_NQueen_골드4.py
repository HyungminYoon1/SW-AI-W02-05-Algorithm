# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

'''
def n_queen(n):

    if n == 1:
        return 1

    total_count = 0 # 총 통과한 횟수
    
    # 첫번째 행에서 시작 위치 결정 
    for x in range(n):
        board = [[True]*n for _ in range(n)] # 보드 초기화
        count = search_position(board, x, 0)
        total_count += count
    return total_count

def search_position(board, x, y): # n은 보드의 위에서부터 차례대로 내려오는 행을 의미(일종의 y 좌표: 0 ~ n-1), x는 해당 행에서 몇 번째 열인지 체크(0 ~ n-1)
    n = len(board)

    # 현재 위치가 이미 불가능한 칸이면 실패
    if not board[y][x]:
        return 0

    # 종료조건: 마지막 칸까지 퀸을 놓을 수 있었다면 성공
    if y == n - 1:
        return 1
    
    # 현재 위치 기준으로 공격 가능한 칸 막기
    new_board = [row[:] for row in board]
    mark_invalid(new_board, x, y)

    count = 0

    # 다음 행에서 가능한 열 탐색
    for next_x in range(n): # 다음 열 중에서 선택 가능한 위치 탐색
        if new_board[y+1][next_x]:
            count += search_position(new_board, next_x, y + 1) # 선택 적용 후 다음 단계로 이동

    return count

# board[][] 가 주어졌을 때 board[y][x] 를 중심으로 가로, 세로, 대각선을 False 처리하는 함수
def mark_invalid(board, x, y):
    n = len(board)

    # 1. 같은 행 False
    for i in range(n):
        board[y][i] = False

    # 2. 같은 열 False
    for i in range(n):
        board[i][x] = False

    # 3. 대각선 방향들
    directions = [
        (1, 1),    # 우하
        (-1, -1),  # 좌상
        (1, -1),   # 우상
        (-1, 1)    # 좌하
    ]

    for dx, dy in directions:
        nx, ny = x, y

        while True:
            nx += dx
            ny += dy

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break

            board[ny][nx] = False

n = int(input())
print(n_queen(n))

'''

# 테스트 케이스
# print(n_queen(1)) # 1
# print(n_queen(2)) # 0
# print(n_queen(3)) # 0
# print(n_queen(4)) # 2
# print(n_queen(5)) # 10
# print(n_queen(8)) # 92

## 결론: 시간 초과로 백준 문제 풀이 실패

'''
매 재귀마다 보드를 복사하기 때문에 입력 크기가 커질수록 이 방식이 불리합니다.
정석은 보드 전체를 안 쓰는 것입니다.

특히 다시 점검해야 할 사고 포인트
이 문제에서 스스로 확인해야 할 질문은 다음입니다.
- 재귀 함수가 무엇을 반환해야 하는가?
- 지금 내가 순회하는 값이 좌표인가, 셀 값인가?
- copy()가 얕은 복사인지 깊은 복사인지 확인했는가?
- 백트래킹에서 상태 복구는 이름 재할당으로 되는가, 아니면 실제 데이터 복원이 필요한가?

'''

## gpt가 제시한 정석 코드

def n_queen_2(n):
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)          # row + col
    diag2 = [False] * (2 * n - 1)          # row - col + n - 1

    def backtrack(row):
        if row == n:
            return 1

        count = 0

        for col in range(n):
            d1 = row + col
            d2 = row - col + n - 1

            if cols[col] or diag1[d1] or diag2[d2]:
                continue

            cols[col] = True
            diag1[d1] = True
            diag2[d2] = True

            count += backtrack(row + 1)

            cols[col] = False
            diag1[d1] = False
            diag2[d2] = False

        return count

    return backtrack(0)

input_num = int(input())
if 1<= input_num and input_num <= 15:
    print(n_queen_2(input_num))

print(n_queen_2(2)) # 0
print(n_queen_2(3)) # 0
print(n_queen_2(4))  # 2
print(n_queen_2(5))  # 10
print(n_queen_2(8))  # 92