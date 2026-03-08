# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


N = int(input())
raw_nums = list(map(int, input().split()))
nums = sorted(raw_nums)
primes_in_nums = []
max_num = nums[N-1]
primes_under_max_num = sieve(max_num)

for num in nums:
    if num in primes_under_max_num:
        primes_in_nums.append(num)

print(len(primes_in_nums))


## gpt 코칭 후 개선한 코드
'''
def sieve(n):
    is_prime = [True] * (n + 1)

    if n >= 0:
        is_prime[0] = False
    if n >= 1:
        is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return is_prime


N = int(input())
nums = list(map(int, input().split()))

is_prime = sieve(max(nums))

count = 0
for num in nums:
    if is_prime[num]:
        count += 1

print(count)
'''

