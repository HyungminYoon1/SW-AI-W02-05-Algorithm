# 정수론 (Number Theory)

## 개요

최대공약수(GCD), 최소공배수(LCM), 소수 판별 등 정수 관련 기본 개념을 다룹니다.

## 최대공약수 (GCD)

**유클리드 호제법**:

```
gcd(a, b) = gcd(b, a % b)
gcd(a, 0) = a
```

```python
def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
```

- 시간 복잡도: O(log min(a, b))

## 최소공배수 (LCM)

```
lcm(a, b) = (a × b) / gcd(a, b)
```

- 정수 나눗셈: `a * b // gcd(a, b)` (오버플로우 주의: `a // gcd(a,b) * b` 형태 권장)

## 확장 유클리드 호제법

`ax + by = gcd(a, b)`를 만족하는 정수 x, y를 구함.  
모듈러 역원, 디오판틴 방정식 등에 활용.

## 소수 판별

- n < 2 → 소수 아님
- 2는 소수
- 2부터 √n까지 나누어 떨어지면 합성수

```python
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True
```

- 시간 복잡도: O(√n)

## 관련 코드

`week2/basic/10_number_theory.py`
