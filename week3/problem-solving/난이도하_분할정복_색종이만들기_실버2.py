# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630


paper = []
size = int(input())
for i in range(size):
    line_list = list(map(int, input().split()))
    paper.append(line_list)    

color_count = [0, 0]

# (x, y)부터 size x size 영역 검사 (x는 행, y는 열 인덱스)
def divide(x, y, size):

    is_area_same_color = True

    # 현재 영역이 모두 같은 색: 갯수 증가
    for i in range(size):
        for j in range(size):            
            if paper[x + i][y + j] != paper[x][y]:
                is_area_same_color = False
                break
            if not is_area_same_color:
                break

    if is_area_same_color:
        color_count[paper[x][y]] += 1 # 기준 좌표의 색상 + 1
        return

    # 아니면 4등분해서 재귀 탐색
    half = size // 2
    divide(x, y, half)
    divide(x, y + half, half)
    divide(x + half, y, half)
    divide(x + half, y + half, half)

divide(0, 0, size)
print(color_count[0])
print(color_count[1])


## gpt가 제시한 최적 코드
