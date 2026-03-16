# 큐 - 가운데를 말해요 (백준 골드2)
# 문제 링크: https://www.acmicpc.net/problem/1655

'''
import heapq

n = int(input())
mid_number = int(input())
left_heap = [-mid_number] # 최대 힙. left_heap[0] 이 가장 큼. 기본 힙은 최대힙이므로 입력값을 음수로 파싱해서 사용
right_heap = [] # 최소 힙. right_heap[0] 이 가장 작음
# left_heap 의 최댓값은 # right_heap의 최솟값보다 작거나 같음

answers = list()
answers.append(mid_number)

for i in range(1, n):
    new_number = int(input())

    # 새로운 숫자를 좌우 힙 길이에 맞게 집어넣음
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -new_number)
    else:
        heapq.heappush(right_heap, new_number)

    # 좌우 힙에서 최대, 최소값을 비교하여 순서가 바뀐 원소 교체
    while -left_heap[0] > right_heap[0]:
        t = -heapq.heappop(left_heap)
        heapq.heappush(right_heap, t)
    
        t = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -t)
    
    mid_number = -left_heap[0]
        
    answers.append(mid_number)

print('\n'.join(map(str, answers)))
'''

'''
위의 코드는 시간 초과로 백준 통과 실패
'''

## gpt 코칭 후 개선한 코드

import heapq
import sys

input = sys.stdin.readline

n = int(input())
mid_number = int(input())
left_heap = [-mid_number] # 최대 힙. left_heap[0] 이 가장 큼. 기본 힙은 최대힙이므로 입력값을 음수로 파싱해서 사용
right_heap = [] # 최소 힙. right_heap[0] 이 가장 작음
# left_heap 의 최댓값은 # right_heap의 최솟값보다 작거나 같음

answers = list()
answers.append(mid_number)

for i in range(1, n):
    new_number = int(input())

    # 새로운 숫자를 좌우 힙 길이에 맞게 집어넣음
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -new_number)
    else:
        heapq.heappush(right_heap, new_number)

    # 좌우 힙에서 최대, 최소값을 비교하여 순서가 바뀐 원소 교체
    if -left_heap[0] > right_heap[0]:
        t = -heapq.heappop(left_heap)
        heapq.heappush(right_heap, t)
    
        t = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -t)
    
    mid_number = -left_heap[0]
        
    answers.append(mid_number)

print('\n'.join(map(str, answers)))