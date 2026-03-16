# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

import math
index = list(map(int, input().split()))

def pow_remain(A, B, C):

    x = A % C
    r_list = [x] # x의 2 거듭제곱을 C 로 나눈 나머지 : [(x^1), (x^2)%C, (x^4)%C, (x^8)%C, ... ]
    n = math.floor(math.log2(B)) # r_list와 순열 Bn 에 담을 원수의 갯수
    
    count = 0
    # r_list 채우기
    while count < n:
        r = r_list[count]
        r_list.append((r*r)%C)
        count += 1
    
    # B = B0 * 2^0 + B1 * 2^1 + ... + Bn * 2^n
    bits_B = list(map(int, bin(B)[2:])) # B 를 2진수로 표현(순열 Bn, Bn-1, ..., B0 순)

    result = 1
    r_index = 0
    while bits_B:
        last_index = bits_B.pop()
        result *= pow(r_list[r_index], last_index, C)
        r_index += 1
    
    return result % C

print(pow_remain(index[0], index[1], index[2]))


## gpt가 개선 코드(최소 수정 버전)

A, B, C = map(int, input().split())

def pow_remain_2(A, B, C):
    x = A % C
    r_list = [x]  # [A^(2^0)%C, A^(2^1)%C, A^(2^2)%C, ...]

    bits_B = list(map(int, bin(B)[2:]))  # B의 이진수 표현
    n = len(bits_B)

    for i in range(1, n):
        r_list.append((r_list[i - 1] * r_list[i - 1]) % C)

    result = 1
    r_index = 0

    while bits_B:
        last_bit = bits_B.pop()  # B0, B1, B2, ... 순서로 꺼냄
        if last_bit == 1:
            result = (result * r_list[r_index]) % C
        r_index += 1

    return result

print(pow_remain_2(A, B, C))



## gpt가 제시한 정석적인 반복형 버전 풀이

A, B, C = map(int, input().split())

def pow_remain_3(A, B, C):
    result = 1
    base = A % C

    while B > 0:
        if B % 2 == 1:
            result = (result * base) % C
        base = (base * base) % C
        B //= 2

    return result

print(pow_remain_3(A, B, C))


## 내장함수로 구현한 치트 풀이
print(pow(*map(int, input().split())))