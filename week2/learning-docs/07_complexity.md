# 복잡도 분석 (Big O)

## 개요

알고리즘의 **시간 복잡도**와 **공간 복잡도**를 Big O 표기법으로 표현하고, 같은 문제를 다양한 복잡도로 해결하는 방법을 비교합니다.

## Big O 표기법

- **의미**: 입력 크기 n에 대해 알고리즘의 수행 시간/공간 **상한(upper bound)**을 표현
- 최고차항만 사용, 상수 계수는 생략
- O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n)

## 중복 원소 찾기: 3가지 방법

### 1. Brute Force (이중 반복문)

- 시간: O(n²)
- 공간: O(k), k = 중복 원소 개수
- 특징: 구현 단순, n이 크면 느림

### 2. 정렬 후 인접 비교

- 시간: O(n log n)
- 공간: O(1) (in-place 정렬 시)
- 특징: 추가 메모리 적음
- **주의**: `nums.sort()`는 원본을 수정함. 원본 보존이 필요하면 `nums_sorted = sorted(nums)` 후 `nums_sorted`로 정렬 후 비교

### 3. 해시 집합 (Hash Set)

- 시간: O(n)
- 공간: O(n)
- 특징: 가장 빠름, 추가 메모리 사용

```python
seen = set()
duplicates = set()
for num in nums:
    if num in seen:
        duplicates.add(num)
    seen.add(num)
```

## 시간-공간 트레이드오프

- 빠른 알고리즘은 보통 더 많은 메모리를 사용
- 문제 제약(메모리, 시간)에 맞춰 방법 선택

## 주의사항

- 방법2에서 `find_duplicates_sorting(nums)` 호출 시 `nums`가 원본이면 정렬 후 원본 배열이 변경됨. 테스트 시 `func(nums[:])`처럼 복사본 전달 권장

## 관련 코드

`week2/basic/07_complexity.py`
