# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470

n = int(input())
solutions = sorted(list(map(int, input().split())))
left_index = 0
right_index = n-1
best_sum = float('inf')
answer = (solutions[left_index], solutions[right_index])

while left_index < right_index:
    current_sum = solutions[left_index] + solutions[right_index]
    
    if abs(current_sum) < abs(best_sum):
        best_sum = current_sum
        answer = (solutions[left_index], solutions[right_index])

    if current_sum > 0:
        right_index -=1
    elif current_sum < 0:
        left_index += 1
    else:
        break

print(answer[0], answer[1])