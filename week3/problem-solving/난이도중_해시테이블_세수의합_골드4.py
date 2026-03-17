# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

'''
5~1000 개의 자연수들로 이루어진 집합 U.
U에서 세 숫자를 골라서 그 합 d가 U의 안에 포함되는 경우 중 가장 큰 d를 찾아라. (세 숫자는 같은 숫자 중복 선택 가능)
'''

'''
풀이 전략
x + y = d - z 로 치환
1. 배열의 모든 두 수의 합을 미리 구해 set으로 저장
2. 어떤 d와 z를 골랐을 때 d - z가 그 저장된 합들 안에 있는지 확인
3. 가장 큰 d부터 내려오면서 확인하면, 처음 찾는 답이 정답

시간 복잡도
- 두 수의 합 만들기: O(N^2)
- d, z 확인: O(N^2)

'''
n = int(input())
num_list = []

for i in range(n):
    num_list.append(int(input()))

sorted_num_list = sorted(num_list)

sum_set = set()

for i in range(n):
    for j in range(i, n):
        sum_set.add(sorted_num_list[i]+sorted_num_list[j])

def get_largest_sum_0f_3_elements(sorted_num_list, sum_set):

    for i in range(n-1, -1, -1): # 가장 큰 숫자부터 카운팅
        d = sorted_num_list[i]
        for j in range(i): # 이미 선택한 i 번째 숫자보다 작거나 같은 수만 검토하면 됨
            z = sorted_num_list[j]

            if (d-z) in sum_set:
                return d
            
    return None

print(get_largest_sum_0f_3_elements(sorted_num_list, sum_set))


## gpt가 제시한 최적화 풀이(위의 풀이와 사실상 동일한 풀이이며 미세 최적화만 추가)

import sys

input = sys.stdin.readline

n = int(input())
numbers = sorted(int(input()) for _ in range(n))

two_sum_set = set()
for i in range(n):
    for j in range(i, n):
        two_sum_set.add(numbers[i] + numbers[j])

for i in range(n - 1, -1, -1):
    d = numbers[i]
    for j in range(i, -1, -1):
        z = numbers[j]
        if d - z in two_sum_set:
            print(d)
            sys.exit()
