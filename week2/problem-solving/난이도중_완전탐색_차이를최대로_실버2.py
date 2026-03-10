# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

'''
완전탐색을 사용한다.
'''

# 인덱스로 실제 거리 측정
def get_route_distance_with(index_list):
    route_distance = 0
    for i in range(len(index_list)-1):
        route_distance += distant[index_list[i]][index_list[i+1]]
            
    return route_distance

# 주어진 리스트로 순열 만들기
def make_permutations(index_list):
    result = []
    visited = [False] * len(index_list)
    path = []

    def dfs():
        if len(path) == len(index_list):
            result.append(path.copy())
            return

        for i in range(len(index_list)):
            if visited[i]:
                continue

            visited[i] = True
            path.append(index_list[i])

            dfs()

            path.pop()
            visited[i] = False

    dfs()
    return result

# 거리 매핑 함수
def map_distance_with_index(num_list):
    size = len(num_list)
    distant_map = [[0] * size for _ in range(size)] # 0으로 초기화
    # 거리 매핑
    for i in range(size):
        for j in range(i+1, size):
            distant_map[i][j] = abs(num_list[i] - num_list[j])
            distant_map[j][i] = distant_map[i][j]
    
    return distant_map

# 입력값 수집
case_count = int(input())
numbers_text = input()
number_list = list(map(int, numbers_text.split()))

biggest_sum = 0 # 거리 최댓값을 저장하는 변수
distant = map_distance_with_index(number_list) # 숫자 간 거리를 매핑한 정보를 담은 리스트
index_list = list(range(len(number_list))) # 순열 조합을 위한 기본 인덱스 리스트 [0, 1, 2, ..., ele_count-1]
all_index_list = make_permutations(index_list) # 모든 인덱스 조합

# 모든 거리 조합을 탐색해서 최댓값 찾기
for index in all_index_list:
    distance = get_route_distance_with(index)
    if distance > biggest_sum:
        biggest_sum = distance

print(biggest_sum)



'''
작성한 코드의 문제점
1. 가장 큰 문제: 순열을 전부 result에 저장함
make_permutations()는 모든 순열을 만든 뒤 result 리스트에 다 넣습니다.
 
하지만 실제로 필요한 것은 순열 전체 목록이 아니라 현재 순열 하나의 점수만 계산해서 최댓값만 갱신하는 것.
즉, 순열을 “저장”할 필요가 없습니다.
DFS를 돌면서 완성된 순간 바로 계산하면 됩니다.

2. 거리 행렬 distant를 만드는 것도 꼭 필요하지 않음
굳이 n x n 행렬을 만들지 않고, 순열이 완성되었을 때 바로 계산해도 됩니다.

3. case_count라는 변수명은 부정확함
입력받는 값은 원소 개수 N 입니다. 따라서 n = int(input()) 이 더 적절합니다.

4. 전역 변수 의존성이 있음
get_route_distance_with() 안에서 distant를 직접 참조합니다.
def get_route_distance_with(index_list):
    route_distance = 0
    for i in range(len(index_list)-1):
        route_distance += distant[index_list[i]][index_list[i+1]]
    
이 함수는 겉으로는 index_list만 받는 것처럼 보이지만, 실제로는 전역 변수 distant가 없으면 동작하지 않습니다.
이건 함수 독립성이 떨어집니다.
차라리 이렇게 해야 합니다.

def get_route_distance_with(index_list, distant):

5. 인덱스 순열을 만들 필요 없이 숫자 순열을 만들면 됨
숫자 자체가 아니라 인덱스를 순열로 만들고 있습니다. 이게 가장 큰 낭비입니다.

* 문제점 요약
1) 모든 순열을 메모리에 저장
2) 불필요한 거리 행렬 생성
3) 인덱스를 통해 한 번 더 우회
4) 전역 변수 의존
5) 변수명 부정확
6) 문제에 비해 설계가 과하게 일반화됨

'''

## gpt 코칭 후 수정한 코드

'''
# DFS 백트래킹으로 순열을 만들되, 저장하지 않고 바로 계산
n = int(input())
nums = list(map(int, input().split()))

visited = [False] * n
path = []
answer = 0

def dfs():
    global answer

    if len(path) == n:
        total = 0
        for i in range(n - 1):
            total += abs(path[i] - path[i + 1])
        answer = max(answer, total)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        path.append(nums[i])
        dfs()
        path.pop()
        visited[i] = False

dfs()
print(answer)

'''