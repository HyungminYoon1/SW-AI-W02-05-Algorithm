# 백트래킹 (Backtracking)

## 개요

**백트래킹**은 모든 경우를 시도하다가 조건에 맞지 않으면 이전 단계로 돌아가 다른 선택을 시도하는 탐색 기법입니다.

## 3단계 패턴

1. **선택(Choose)**: 후보를 현재 선택에 추가
2. **탐색(Explore)**: 재귀로 다음 단계 진행
3. **선택 취소(Unchoose)**: 재귀 종료 후 현재 선택을 되돌림

```python
def backtrack(start, current):
    if len(current) == k:  # base case
        result.append(current.copy())
        return
    for i in range(start, n+1):
        current.append(i)           # 1. 선택
        backtrack(i+1, current)     # 2. 탐색
        current.pop()               # 3. 취소
```

## 조합 vs 순열

| 구분 | 조합 | 순열 |
|------|------|------|
| 순서 | 무관 ([1,2] = [2,1]) | 중요 |
| 탐색 | start 이후만 | 방문하지 않은 모든 후보 |

## 참고

- `result.append(current.copy())` 사용: 참조가 저장되지 않도록 복사본 저장

## 활용 예시

- 조합/순열 생성
- N-Queens
- 부분집합, 스도쿠 등

## 관련 코드

`week2/basic/06_backtracking.py`
