# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
'''

# 이 코드는 불필요한 과정이 많아 시간 초과로 백준 통과 실패

from collections import deque

order_que = deque()
original_text = input()
order_count = int(input())
for i in range(order_count):
    order_que.append(input())

def editor(text, order_que):
    cursor_index = len(text)

    while order_que:
        order = list((order_que[0].split()))
        if order[0] == 'L':
            if cursor_index > 0:
                cursor_index -= 1
        elif order[0] == 'D':
            if cursor_index < len(text):
                cursor_index += 1
        elif order[0] == 'B':
            if cursor_index > 0:
                text = text[1:]
                cursor_index -= 1
        elif order[0] == 'P':
            text = text[:cursor_index] + order[1] + text[cursor_index:]

        order_que.popleft()

    return text

print(editor(original_text, order_que))
'''


## gpt 코칭 후 개선한 코드
# sys.stdin.readline 사용
# 커서 위치를 기준으로 좌우 스택 만듦 -> 오른쪽 스택은 원래 문자열과 반전됨(pop(0)을 사용하지 않아 연산 횟수 감소)

import sys

input = sys.stdin.readline

left = list(input().strip())
right = []

for i in range(int(input())):
    order = input().split()

    if order[0] == 'L':
        if left:
            right.append(left.pop())
    elif order[0] == 'D':
        if right:
            left.append(right.pop())
    elif order[0] == 'B':
        if left:
            left.pop()
    elif order[0] == 'P':
            left.append(order[1])

print(''.join(left + right[::-1]))
