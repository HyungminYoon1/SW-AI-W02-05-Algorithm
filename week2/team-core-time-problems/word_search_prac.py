
# Input: 
example_board = [["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]]
example_word = "ABFDE"

given_text = example_word
board = example_board

# Expected Output: true

# 보드 정보
width = len(example_board[0]) #4 (0, 1, 2, 3)
height = len(example_board) #3 (0, 1, 2)

# 이미 지나온 보드칸 좌표를 저장하는 공간
stacked_board_location = []

def is_text_included(board, given_text):

    # 전역 실패 여부 검증
    # 총 텍스트 길이가 보드 범위에서 벗어나면 False
    if len(given_text) > width * height:
        return False

    # 최초 탐색 시작 위치 결정
    for i in range(height): # 0, 1, 2 => y 좌표
        for j in range(width): # 0, 1, 2, 3 => x 좌표
            if board[i][j] == given_text[0]:
                stacked_board_location.clear() # 첫 글자 시작시마다 지나온 경로 초기화
                result = recursive_text_adder("", j, i) # 재귀적 탐색 시작
                if result:
                    return True

    # 최종적으로 결과가 없으면 False
    return False

def recursive_text_adder(making_text, x, y):
    
    # 1. 범위 검사 먼저
    if x < 0 or y < 0 or x >= width or y >= height:
        return False

    # 2. 방문 검사
    if (y, x) in stacked_board_location:
        return False

    # 3. 문자 검사
    if board[y][x] != given_text[len(making_text)]:
        return False
    
    # 4. 방문 처리
    stacked_board_location.append((y, x))
    making_text += board[y][x]
    print(making_text)
    # 5. 완성 검사
    if making_text == given_text:
        return True
    
    # 4방향 탐색 시도
    r1 = recursive_text_adder(making_text, x+1, y)
    if r1:
        return True
    r2 = recursive_text_adder(making_text, x-1, y)
    if r2:
        return True
    r3 = recursive_text_adder(making_text, x, y+1)
    if r3:
        return True
    r4 = recursive_text_adder(making_text, x, y-1)
    if r4:
        return True

    # 최종 실패하면 현재 방문 취소
    stacked_board_location.pop()
    return False

print(is_text_included(example_board, example_word))