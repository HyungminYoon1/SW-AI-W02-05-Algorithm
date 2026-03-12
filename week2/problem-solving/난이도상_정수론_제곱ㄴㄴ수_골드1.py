# # 정수론 - 제곱 ㄴㄴ 수 (백준 골드1)
# # 문제 링크: https://www.acmicpc.net/problem/1016



# # 4의 배수 제거, 9의 배수 제거, 25의 배수 제거, ..., 소수 p^2 의 배수 제거

# # 사용할 소수는 최대 root(max) 까지만 구하면 됨.

# # 소수를 구할 때 에라토스테네스의 체 사용 (자연수-boolean 매핑 2개 생성, 하나는 소수 매핑 용도, 다른 수는 제곱ㄴㄴ수 매핑 용도)

# # 에라토스테네스를 체를 사용할 때 p^2 이상이 곱해지는 숫자에 대해서는 제곱 ㄴㄴ 수의 boolean 매핑을 False 처리 

# # p = [2, 3, 5, ..., math.floor(math.sqrt(max)) 이하의 가장 큰 소수]

# import math

# input_list = list(map(int,input().split()))
# min = input_list[0]
# max = input_list[1]
# diff = max - min

# is_prime = [True] * (max+1) # 소수 boolean 매핑
# is_free_square = [True] * (max+1) # 제곱ㄴㄴ수 boolean 매핑

# # 에라토스테네스의 체
# def sieve(n):

#     limit_num = math.floor(math.sqrt(n))

#     is_prime[0] = False
#     is_prime[1] = False
#     is_prime[2] = True
#     is_prime[3] = True

#     for i in range(4, n+1, 2):
#         is_prime[i] = False

#     for i in range(3, limit_num+1, 2):
#         if is_prime[i]:
#             j = i
#             while(j <= limit_num):
#                 is_prime[i*j] = False
#                 j += 2
#     return



# # 제곱수의 배수를 거르는 체
# def free_square_count(min_num, max_num):

#     prime_supremum = math.floor(math.sqrt(max_num)) # p*p <= max 을 만족하는 가장 큰 소수의 상한
#     sieve(prime_supremum)
    
#     count = 0

#     for i in range(2, prime_supremum + 1):
#         if is_prime[i]:
#             square_i = i*i
#             min_bound = (min_num//square_i)*square_i # min_num 보다 크거나 같은 최소의 i^2 의 배수
#             max_bound = (max_num//square_i)*square_i # max_num 보다 작거나 같은 최대의 i^2 의 배수
#             j = min_bound
#             while(j <= max_bound):
#                 is_free_square[min_bound] = False # 제곱ㄴㄴ수 매핑에 False 처리
#                 j += square_i

#     for i in range(min_num, max_num+1):
#         if is_free_square[i]:
#             count += 1
#     print(count)

# free_square_count(min, max)

'''
재작성
'''

import math

min_num, max_num  = list(map(int, input().split()))
is_free_square = [False] * (max_num-min_num+1) # 제곱ㄴㄴ수 boolean 매핑

def free_square_count(min_num, max_num):

    limit = math.floor(math.sqrt(max_num)) # i*i <= max_num을 만족하는 i의 최댓값

    for i in range(2, limit + 1):
        square_i = i*i
        start = ((min_num + square_i - 1) // square_i) * square_i # min_num 이상인 square의 첫 배수
        j = start
        while(j<=max_num):
            is_free_square[j-min_num] = True # 제곱수는 True 처리
            j += square_i

    print(is_free_square.count(False))

free_square_count(min_num, max_num)
