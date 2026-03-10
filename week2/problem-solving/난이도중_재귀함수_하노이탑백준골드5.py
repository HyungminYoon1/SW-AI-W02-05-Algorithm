# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

import math

def hanoi_count(n):
    return int(math.pow(2, n)) - 1

def hanoi_process(n):

    if n in hanoi_stack:
        return hanoi_stack.get(n)
    
    former_process = hanoi_process(n-1) # 재귀 탐색

    # 앞과 뒤에 붙여넣을 것 생성
    prefix = [
        [3 if x == 2 else 2 if x == 3 else x for x in row] for row in former_process
    ] # 2와 3 교체
    suffix = [
        [1 if x == 2 else 2 if x == 1 else x for x in row] for row in former_process
    ] # 1과 2 교체
    
    result_step = prefix + [[1, 3]] + suffix
    hanoi_stack[n] = result_step
    return result_step

hanoi_stack = {1:[[1, 3]]}

layer_count = int(input())

print(hanoi_count(layer_count))
result = hanoi_process(layer_count)

for element in result:
    print(*element)

''' 문제 해결방법 고민
n = 1:
1 3 = 가장 큰 원판

n = 2:
1 2 처음에 1은 항상 고정, 그 다음 숫자는 n이 짝수이면 2, 홀수이면 3
1 3 = 가장 큰 원판 고정
2 3

n = 3:
1 3 1단계 전의 구조와 같으나 2와 3만 교체한 구조
1 2 
3 2
1 3 = 가장 큰 원판
2 1 1단계 전의 구조와 같으나 이전 단계에서는 1에 쌓였있던 대상을 3으로 옮긴 반면, 현재 단계에서는 2에 쌓여있던 대상을 3으로 옮겨야 함. 따라서 이전 단계의 1과 2 교체
2 3
1 3

'''
# 가장 가운데는 1 3 으로 고정. 그 앞 부분은 이전 단계 복사 후 2와 3만 교환하고, 가운데 다음 부분은 이전 단계 복사 후 1과 2만 교환


## 백준에 넣었으나 메모리 초과로 실패

## gpt 코칭 후 수정한 코드
'''
def hanoi_count(n):
    return (1 << n) - 1   # 2^n - 1

def hanoi(n, start, end, aux):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, aux, end)
    print(start, end)
    hanoi(n - 1, aux, end, start)

n = int(input())

print(hanoi_count(n))
hanoi(n, 1, 3, 2)
'''