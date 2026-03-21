# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)
preorder_list = list(map(int, sys.stdin.read().split()))

def make_postorder(start, end):
    
    # 재귀 종료 조건
    if start > end:
        return []

    result = []

    # 루트 찾기
    root = preorder_list[start]
    slice_index = end + 1 # 초기값은 배열 접근 용도가 아니라, 루트보다 큰 값이 하나도 없으면 '오른쪽 서브트리가 없음'을 표현하는데 사용
    for i in range(start, end+1):
        if preorder_list[i] > root:
            slice_index = i
            break

    # 왼쪽 구간
    left_start = start+1
    left_end = slice_index - 1

    # 오른쪽 구간
    right_start = slice_index
    right_end = end

    # 왼쪽 재귀
    left = make_postorder(left_start, left_end)
    result.extend(left)

    # 오른쪽 재귀
    right = make_postorder(right_start, right_end)
    result.extend(right)

    # 루트 추가
    result.append(root)

    return result

result_list = make_postorder(0, len(preorder_list) - 1)
for result in result_list:
    print(result)

'''
현재 코드의 문제점

1) 현재 코드가 각 재귀 호출마다 루트보다 큰 값이 처음 나오는 위치를 선형 탐색하고 있기 때문에
시간복잡도는 최악의 경우 O(N^2) 가 될 수 있습니다.
예를 들어 입력이 한쪽으로 치우친 BST 모양이면, 길이 N 구간에서 찾고, 그다음 N-1, N-2... 식으로 반복될 수 있습니다.
이를 해결하기 위해 전역 인덱스 하나를 두고 현재 서브트리에서 허용되는 값 범위 (min_val, max_val) 를 넘겨가며
전위 순회 배열을 한 번만 앞에서부터 읽는 방식을 사용하면 각 원소를 거의 한 번씩만 처리해서 O(N) 에 가깝게 만들 수 있습니다.
즉, '현재 값이 이 서브트리에 들어올 수 있으면 소비하고, 아니면 상위 호출로 돌려보내는 방식'입니다.

2) 매번 result 리스트를 새로 만들고 extend 하는 방식이라, 출력만 하면 되는 문제치고는 메모리 사용이 더 있습니다.
이 문제에서 리스트를 반환하기보다 재귀 끝에서 바로 print 하면 메모리 사용을 줄일 수 있습니다.

'''

## gpt가 제안한 개선 코드

# 메모리 절약형 정석 풀이: 결과 리스트를 만들지 않고 바로 출력

import sys

sys.setrecursionlimit(10**6)
preorder_list = list(map(int, sys.stdin.read().split()))

def print_postorder(start, end):
    if start > end:
        return

    root = preorder_list[start]
    right_start = end + 1

    for i in range(start + 1, end + 1):
        if preorder_list[i] > root:
            right_start = i
            break

    print_postorder(start + 1, right_start - 1)
    print_postorder(right_start, end)
    print(root)

print_postorder(0, len(preorder_list) - 1)


## gpt가 제안한 최적 코드

# 범위 제한 + 전역 인덱스 풀이
import sys

sys.setrecursionlimit(10**6)
preorder_list = list(map(int, sys.stdin.read().split()))
index = 0

def print_postorder_by_range(lower, upper):
    global index

    if index >= len(preorder_list):
        return

    value = preorder_list[index]
    if value < lower or value > upper:
        return

    index += 1

    print_postorder_by_range(lower, value - 1)
    print_postorder_by_range(value + 1, upper)
    print(value)

print_postorder_by_range(float('-inf'), float('inf'))

