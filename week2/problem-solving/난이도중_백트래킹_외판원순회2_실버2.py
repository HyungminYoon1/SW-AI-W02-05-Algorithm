# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971


city_count = int(input())
cost_matrix = [] # 이동 비용 매트릭스

for i in range(city_count):
    cost_matrix.append(list(map(int, input().split())))

# 도시 수에 따른 기본 인덱스 리스트
city_index = list(range(city_count))

path = [0]
visited = [False] * city_count
visited[0] = True
mimimum_cost = float('inf') # 최댓값으로 초기화

def dfs():
    global mimimum_cost
    
    # 경로가 다 차면 비용 계산
    if len(path) == city_count:
        route_cost = 0
        for i in range(city_count - 1):
            cost = cost_matrix[path[i]][path[i+1]]
            if cost == 0: # 갈 수 없는 곳 검증 로직
                return 
            route_cost += cost
        last_cost = cost_matrix[path[-1]][path[0]] # 마지막 도시에서 출발도시로 복귀 이동
        if last_cost == 0: # 갈 수 없는 곳 검증 로직
            return 
        route_cost += last_cost
        mimimum_cost = min(mimimum_cost, route_cost) # 경로 비용 최솟값 갱신
        return 

    # 경로가 안 차면 재귀 탐색
    for i in range(city_count):
        if visited[i]:
            continue

        visited[i] = True
        path.append(city_index[i]) # 도시 추가

        dfs() # 재귀 탐색

        path.pop() # 취소(이전 도시)
        visited[i] = False
    return

dfs()
print(mimimum_cost)


'''
현재 코드는 탐색 중에 불필요한 연산이 꽤 있습니다.
핵심 문제는 두 가지입니다.

현재 코드의 비효율

1) 리프 노드에서만 비용을 한꺼번에 계산함

지금은 path가 완성된 뒤에야 전체 경로 비용을 다시 계산합니다.
즉, 순열 하나가 완성될 때마다: 
for i in range(city_count - 1):
를 다시 돌기 때문에,
각 순열마다 추가로 O(N)이 붙습니다.
외판원 순회 2는 사실상 O((N-1)!)에 가까운 탐색인데, 여기에 매번 경로 합산까지 다시 하면 더 느려집니다.

2) 가지치기(pruning)가 없음

현재까지 누적 비용이 이미 minimum_cost 이상이면,
그 이후를 더 탐색할 이유가 없습니다.
그런데 지금 코드는 끝까지 다 내려가 본 뒤에야 비교합니다.

3) 갈 수 없는 간선을 너무 늦게 검증함

cost_matrix[path[i]][path[i+1]] == 0 여부를 마지막에 확인합니다.
사실 이건 도시를 추가하는 순간 바로 걸러낼 수 있습니다.

4) city_index[i]는 불필요

city_index = list(range(city_count)) 를 만들어 놓고 path.append(city_index[i]) 를 하는데,
그냥 path.append(i) 와 동일합니다.

즉, 이 리스트는 없어도 됩니다.

## 가장 직접적인 최적화 방향
- dfs(current_city, depth, current_cost) 형태로 변경
- 도시를 이동할 때마다 비용을 누적
- current_cost >= minimum_cost 이면 즉시 중단
- 이동 불가능한 간선(0)은 재귀 호출 전에 제외
- 마지막 도시까지 왔을 때만 출발점 복귀 가능 여부 검사

'''


## gpt 코칭 후 수정한 코드

'''
import sys
input = sys.stdin.readline

city_count = int(input())
cost_matrix = [list(map(int, input().split())) for _ in range(city_count)]

visited = [False] * city_count
visited[0] = True

minimum_cost = float('inf')


def dfs_2(current_city, depth, current_cost):
    global minimum_cost

    # 가지치기 1: 이미 최소 비용보다 크거나 같으면 더 볼 필요 없음
    if current_cost >= minimum_cost:
        return

    # 모든 도시를 방문한 경우
    if depth == city_count:
        back_cost = cost_matrix[current_city][0]  # 시작 도시로 복귀
        if back_cost != 0:
            minimum_cost = min(minimum_cost, current_cost + back_cost)
        return

    # 다음 도시 탐색
    for next_city in range(1, city_count):  # 0은 시작점이므로 다시 방문 불필요
        if visited[next_city]:
            continue

        move_cost = cost_matrix[current_city][next_city]

        # 가지치기 2: 애초에 갈 수 없는 길이면 탐색 중단
        if move_cost == 0:
            continue

        visited[next_city] = True
        dfs_2(next_city, depth + 1, current_cost + move_cost)
        visited[next_city] = False


dfs_2(0, 1, 0)
print(minimum_cost)

'''