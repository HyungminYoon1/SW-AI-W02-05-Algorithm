# 연결 리스트 (Linked List)

## 개요

**연결 리스트**는 노드(Node)가 데이터와 다음 노드를 가리키는 포인터로 연결된 선형 자료구조입니다. 배열과 달리 연속된 메모리 없이 노드들이 링크로 연결됩니다.

## 핵심 원리

- **Node**: `data`와 `next`(다음 노드를 가리키는 포인터)
- **Head**: 리스트의 첫 번째 노드
- **Tail**: 리스트의 마지막 노드 (단순 연결 리스트에서 `next`는 `None`)

## 구조

```
Head
  ↓
[1] → [2] → [3] → None
```

## 단순 연결 리스트 vs 이중 연결 리스트

| 구분 | 단순 연결 리스트 | 이중 연결 리스트 |
|------|------------------|------------------|
| 포인터 | next만 | next, prev |
| 역순 탐색 | 불가 | 가능 |

## 기본 연산

| 연산 | 설명 | 시간 복잡도 |
|------|------|-------------|
| append | 끝에 추가 | O(n) (tail 찾기) / tail 포인터 유지 시 O(1) |
| prepend | 앞에 추가 | O(1) (head 업데이트 필요) |
| search | 값 찾기 | O(n) |
| insert | 특정 위치 삽입 | O(n) |
| delete | 노드 삭제 | O(n) |

## 배열과 비교

| 구분 | 배열 | 연결 리스트 |
|------|------|-------------|
| 메모리 | 연속 | 분산 |
| 인덱스 접근 | O(1) | O(n) |
| 삽입/삭제 (앞/중간) | O(n) | O(1) (위치 알 때) |
| 메모리 사용 | 고정 또는 동적 | 노드마다 포인터 추가 |

## 구현 힌트

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        # head가 None이면 head = new_node
        # 아니면 마지막 노드까지 이동 후 next 연결
```

## 최적화: tail 포인터

`self.tail`을 유지하면 `append`를 O(1)로 만들 수 있음. 새 노드 추가 시 `tail.next = new_node`, `tail = new_node`로 갱신.

## 주의사항

- **prepend, 맨 앞 삽입 시**: `new_node.next = head`, `head = new_node`로 head를 반드시 업데이트
- **맨 앞 노드 삭제 시**: `head = head.next`로 head 갱신

## 관련 코드

`week3/basic/08_linked_list.py`
