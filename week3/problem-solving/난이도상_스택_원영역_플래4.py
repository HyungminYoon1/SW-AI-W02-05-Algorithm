# 스택 - 원 영역 (백준 플래4)
# 문제 링크: https://www.acmicpc.net/problem/10000

'''
원이 없을 때: 기본 1개 (전체 영역)
원이 1개일 때: 1 추가
원이 2개일 때: 1 추가
원이 n개일 때: 1 추가 # 다만 기존에 존재하는 원의 지름을 다른 원들이 모두 차지할 경우 해당 원이 추가하는 영역은 2가 됨.

해결 방안
1) 원의 지름 (x-r, x+r)을 시작 좌표 순으로 소팅
2) 각각의 원의 지름이 그 내부에 존재하는 작은 원들의 지름의 합으로 표현 가능한지 검토(가능시 갯수 +1)

'''

import sys
input = sys.stdin.readline

def find_next_chain(start, end, segments, idx):
    for i in range(idx, len(segments)):
        s, e = segments[i]
        if s < start:
            continue
        if s > start: # 정렬되어 있으므로 이후 선분은 더 볼 필요가 없음
            break
        if e == end: # start와 이어지는 선분이 끝까지 도달함
            return True
        if find_next_chain(e, end, segments, i + 1):
            return True
    return False

diameters = []
circle_count = int(input())

for i in range(circle_count):
    x, r = map(int, input().split())
    diameter_tuple = (x-r, x+r)
    diameters.append(diameter_tuple)

diameters.sort(key=lambda t: (t[0], -t[1])) # x-r 오름차순, x+r 내림차순으로 소팅

area_count = 1 + circle_count # 기본적으로 최소한 원의 갯수 + 1 만큼 공간이 존재.

# 선분(지름)이 그 내부에 위치한 다른 선분의 합으로 표현이 가능한지 확인

for i in range(circle_count):
    partial_diameter_list = []
    start_point = diameters[i][0]
    end_point = diameters[i][1]
    for j in range(i+1, circle_count):
        if diameters[j][0] >= end_point:
            break
        if start_point <= diameters[j][0] and diameters[j][0] < end_point and diameters[j][1] <= end_point:
            partial_diameter_list.append(diameters[j])
        
    # 후보가 하나도 없을 때만 건너뛴다.
    if partial_diameter_list == []:
        continue
    if find_next_chain(start_point, end_point, partial_diameter_list, 0):
        area_count += 1

print(area_count)

'''
시간 초과로 백준 통과 실패
'''

## gpt가 제시한 개선 코드 (O(n^2) 풀이) -> 시간 초과로 실패

import sys
input = sys.stdin.readline

diameters = []
n = int(input())

for _ in range(n):
    x, r = map(int, input().split())
    diameters.append((x - r, x + r))

diameters.sort(key=lambda t: (t[0], -t[1]))

area_count = 1 + n

for i in range(n):
    start_point, end_point = diameters[i]
    current = start_point

    for j in range(i + 1, n):
        s, e = diameters[j]

        if s >= end_point:
            break

        if s == current and e <= end_point:
            current = e
            if current == end_point:
                area_count += 1
                break

print(area_count)


## gpt가 제시한 정석 풀이 (O(n log n))
'''
원을 “이벤트 점”으로 바꿔 스택으로 처리하는 것

이 풀이의 아이디어는:
- 원 하나가 닫힐 때 기본적으로 영역 +1
- 그 원 내부가 다른 원들로 정확히 꽉 찼다면 추가로 +1
- 이를 스택으로 중첩 구조에 맞게 관리

'''

import sys
input = sys.stdin.readline

n = int(input())
events = []

for _ in range(n):
    x, r = map(int, input().split())
    left = x - r
    right = x + r
    events.append((left, 0))   # 여는 점
    events.append((right, 1))  # 닫는 점

events.sort(key=lambda x: (x[0], -x[1]))

stack = []
area_count = 1

for pos, typ in events:
    if typ == 0:
        stack.append([pos, 0]) # [left_position, sum_of_child_widths]
    else:
        left, inner_sum = stack.pop()
        width = pos - left

        area_count += 1
        if inner_sum == width: # inner_sum은 이 원 내부에 들어 있던 자식 원들이 닫힐 때마다 누적해서 저장해둔 값
            area_count += 1

        if stack:
            stack[-1][1] += width # 방금 막 닫힌 원의 지름 길이 width를, 바깥 부모 원의 inner_sum에 더한다
            # 현재 닫힌 원의 바로 바깥 부모에 대하여, 그 내부 자식 지름의 합에 방금 닫힌 자식 원의 지름만큼 더함을 의미
print(area_count)