# 정수론 - 골드바흐의 추측 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/9020

'''
[문제 내용]
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.
2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.

'''

'''
해결방안 고안
0. 테스트 케이스에 제시된 짝수 중 최대 숫자를 n 으로 놓는다.
1. n 이하의 모든 자연수에 대해 소수 여부 매핑을 작성한다.
2. 위의 매핑에서 n//2 을 확인하여 그 값이 소수이면 종료. 아니면 숫자를 하나씩 늘려가며 n//2-k, n//2+k 를 확인한다.
3. 모두 소수인 페어를 찾으면, 해당 페어 (n//2-k, n//2+k)를 출력한다.

*n//2 이하의 소수의 매핑을 최단시간에 만드는 방법으로 에라토스테네스의 체를 이용한다.

'''

import math

prime_dict = {}

def sieve(n):
    prime_dict = {}

    if n >= 1:
        prime_dict[1] = False
    if n >= 2:
        prime_dict[2] = True

    for i in range(3, n + 1, 2):
        prime_dict[i] = True

    for i in range(4, n + 1, 2):
        prime_dict[i] = False
    
    start = 3
    limit = int(math.sqrt(n))
    while start <= limit:
        if prime_dict[start]==True:
            for j in range(start*start, n+1, start):
                prime_dict[j] = False
        start += 2

    return prime_dict

def is_prime(num):
    return prime_dict[num]

def find_prime_pair(num):
    half_num = num//2
    if is_prime(half_num):
        return half_num, half_num
    
    for i in range(1, half_num):
        if is_prime(half_num-i) and is_prime(half_num+i):
            return half_num-i, half_num+i
    
    return None


case_count = int(input())
even_list = []

for _ in range(case_count):
    even_list.append(int(input()))

prime_dict = sieve(max(even_list))

for element in even_list:
    result = find_prime_pair(element)
    if result:
        print(*result)


## gpt 코칭

'''
현재 코드의 sieve()는 구조적으로 복잡하고 오류 가능성이 있습니다.
가장 안정적인 체 구현은 다음 형태입니다.

def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i*i, n + 1, i):
                prime[j] = False

    return prime

그리고 dict 대신 list를 쓰는 것이 표준적입니다.

추가로 코드 설계 문제가 있습니다.
def is_prime(num):
    return prime_dict[num]
는 전역 변수 의존입니다.
좋은 설계는 아닙니다.

더 좋은 형태:
def is_prime(num, prime):
    return prime[num]

매개변수 방식이 더 좋은 이유:
1. 함수가 독립적
2. 테스트 가능
3. 재사용 가능
4. 전역 상태 의존 없음
'''

## gpt 코칭 후 수정한 코드

'''
prime = []

def sieve(n):
    prime = [True] * (n + 1)

    if n >= 0:
        prime[0] = False
    if n >= 1:
        prime[1] = False

    for i in range(4, n + 1, 2):
        prime[i] = False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return prime

def find_prime_pair(num, prime):
    half = num // 2
    for a in range(half, 1, -1):
        b = num - a
        if prime[a] and prime[b]:
            return a, b
    return None

case_count = int(input())
even_list = [int(input()) for _ in range(case_count)]

prime = sieve(max(even_list))

for element in even_list:
    result = find_prime_pair(element, prime)
    if result is not None:
        print(*result)
'''