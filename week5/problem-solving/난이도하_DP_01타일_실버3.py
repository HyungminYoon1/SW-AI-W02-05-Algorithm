# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

n = int(input())

def fib(n):
    
    if n == 1 or n == 2:
        return n

    a, b = (1, 2)

    for i in range(3, n+1):
        a, b = b, (a + b)  % 15746

    return b

print(fib(n))