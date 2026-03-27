# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

n, k = map(int, input().split()) # n: 동전 종류, k: 가치합

# 동전 종류 리스트 초기화
money_units = []
for i in range(n):
    money_units.append(int(input()))

total_count = 0

for money_unit in reversed(money_units):
    unit_count = k // money_unit
    k = k % money_unit
    total_count += unit_count

if k != 0:
    raise ValueError("값이 동전으로 나누어 떨어지지 않습니다.")
else:
    print(total_count)
