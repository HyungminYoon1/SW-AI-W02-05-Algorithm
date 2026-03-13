# 이분 탐색 (Binary Search)

## 개요

**이분 탐색**은 정렬된 배열에서 특정 값을 효율적으로 찾는 탐색 알고리즘입니다. 배열을 반으로 나누어 탐색 범위를 절반씩 줄여가며 원하는 값을 찾습니다.

## 핵심 원리

- 정렬된 배열에서만 사용 가능
- `left`, `right` 포인터로 탐색 범위 관리
- 매 단계마다 중간값(`mid`)과 target 비교
- 비교 결과에 따라 탐색 범위를 절반으로 축소

## 알고리즘 동작

```
1. left = 0, right = len(arr) - 1
2. left <= right 일 때까지 반복:
   - mid = left + (right - left) // 2  (오버플로우 방지, Python에선 (left+right)//2도 가능)
   - arr[mid] == target → mid 반환
   - arr[mid] < target → left = mid + 1
   - arr[mid] > target → right = mid - 1
3. 찾지 못하면 -1 반환
```

## 시간 복잡도

| 구분 | 복잡도 |
|------|--------|
| 평균/최선/최악 | O(log n) |

매 단계마다 탐색 범위가 절반으로 줄어들어 로그 시간에 탐색이 완료됩니다.

## 활용 예시

- 정렬된 배열에서 값 검색
- **lower_bound**: target 이상인 첫 번째 위치
- **upper_bound**: target 초과인 첫 번째 위치
- 이진 탐색을 활용한 파라미터 탐색 (정답 후보 범위를 이분으로 좁혀나감)

## 구현 힌트

```python
# left, right 포인터 사용
# mid = (left + right) // 2
# arr[mid]와 target 비교하여 범위 조정
```

## 관련 코드

`week3/basic/01_binary_search.py`
