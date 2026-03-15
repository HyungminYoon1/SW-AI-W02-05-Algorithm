# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

'''
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내기
'''

# 이분탐색을 사용한 풀이
def binary_search(sorted_num_list, target):
    left = 0
    right = len(sorted_num_list)-1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_num_list[mid] == target:
            return 1
        elif sorted_num_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return 0

n_count = int(input())
element_list = sorted(map(int, input().split()))
target_count = int(input())
target_items = map(int, input().split())

for target in target_items:
    print(binary_search(element_list, target))
        

# 최적 풀이
# n_count = input()
# element_set = set(map(int, input().split()))
# target_count = input()
# target_items = map(int, input().split())

# for target in target_items:
#     print(1 if target in element_set else 0)



