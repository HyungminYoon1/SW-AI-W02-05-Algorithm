# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

'''
1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
1) 제일 위에 있는 카드를 바닥에 버린다.
2) 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
3) 카드가 1장이 남을 때까지 1번과 2번을 반복
요구사항: n이 주어졌을 때, 제일 마지막에 남게 되는 카드 번호 출력
'''

from collections import deque

n = int(input())
q = deque(range(1, n + 1))

while len(q) > 1:
    q.popleft()
    if q[0]:
        q.append(q.popleft())

print(q[0])