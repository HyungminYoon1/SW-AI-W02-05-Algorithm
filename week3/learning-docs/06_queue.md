# 큐 (Queue)

## 개요

**큐**는 FIFO(First In First Out, 선입선출) 구조의 자료구조입니다. 가장 먼저 넣은 데이터가 가장 먼저 꺼내집니다.

## 핵심 원리

- **Enqueue**: 큐의 뒤에 데이터 추가
- **Dequeue**: 큐의 앞에서 데이터 제거
- **Front**: 맨 앞 데이터 조회

## 비유

대기열, 프린터 대기열과 같습니다. 먼저 온 순서대로 처리됩니다.

## 파이썬 구현

### collections.deque 사용 (권장)

```python
from collections import deque

queue = deque()
queue.append(x)      # enqueue
queue.popleft()      # dequeue
queue[0]             # front
```

### 리스트 사용

```python
queue = []
queue.append(x)      # enqueue
queue.pop(0)         # dequeue (O(n) - 비효율적)
```

> `pop(0)`은 O(n)이므로 데이터가 많으면 `deque` 사용을 권장합니다.

## 시간 복잡도 (deque 기준)

| 연산 | 복잡도 |
|------|--------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Front | O(1) |

## 활용 예시

- 프린터 대기열
- BFS(너비 우선 탐색)
- 작업 스케줄링
- 메시지 큐

## 관련 코드

`week3/basic/06_queue.py`
