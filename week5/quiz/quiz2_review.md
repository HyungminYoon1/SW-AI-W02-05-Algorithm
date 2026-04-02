# 문제
2. 아래 파이썬 코드는 n이 주어졌을 때, n번째 피보나치 수를 구하는 하향식 재귀 + 메모이제이션 방식을 구현하였다. 빈칸을 채워 코드를 완성하시오.

memo = {}

def fib(n):

    if n <= 1:

        return n

    if n not in memo:

        ____________________________________

    return memo[n]

---

# 답변
memo[n] = fib(n-2) + fib(n-1)

---

# 정답
memo[n] = fib(n-1) + fib(n-2)