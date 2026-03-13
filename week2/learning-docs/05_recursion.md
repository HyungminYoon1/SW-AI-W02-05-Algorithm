# 재귀 함수 (Recursion)

## 개요

**재귀 함수**는 함수가 자기 자신을 호출하는 방식입니다.  
Base case(종료 조건)와 Recursive case(재귀 호출)로 정의합니다.

## 핵심 구성

1. **Base Case**: 재귀를 멈추는 조건 (종료)
2. **Recursive Case**: 자기 자신을 더 작은 문제로 호출

## 팩토리얼

```
n! = n × (n-1)!
0! = 1, 1! = 1
```

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

## 피보나치 수열

```
fib(0) = 0, fib(1) = 1
fib(n) = fib(n-1) + fib(n-2)
```

```python
def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

## 주의사항

- **Base case 필수**: 없으면 재귀가 끝나지 않아 무한 호출 → 스택 오버플로우 발생
- **피보나치 단순 재귀**: O(2^n)으로 n이 크면 매우 느림. DP(동적 계획법)나 메모이제이션으로 O(n)으로 개선 가능
- **재귀 깊이 제한**: 파이썬 기본 약 1000회. 매우 깊은 재귀는 반복문으로 전환 고려

## 관련 코드

`week2/basic/05_recursion.py`
