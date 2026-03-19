'''
4.고정 크기 배열(예: 크기 10)만 사용하여, 요소를 이동시키지 않고 O(1)로 삽입/삭제가 가능한 큐를 설계한다면 어떻게 해야할까? 설계 방식을 설명하고 간단하게 파이썬 혹은 수도 코드로 enque, deque 함수를 만들어 보시오.
'''

# 작성한 응답
'''

'''

# 올바른 답

'''
1. 문제 정의
요구사항:
- 고정 크기 배열만 사용
- 요소 이동 없음
- 삽입 / 삭제 O(1)

→ 일반 큐로는 불가능 (앞에서 pop 시 shift 필요)
→ 해결 방법: 원형 큐 (Circular Queue)

2. 핵심 개념 (원형 큐)
- 배열을 원형으로 연결된 것처럼 사용
- 끝에 도달하면 다시 처음으로 돌아감
- 인덱스를 % (mod) 연산으로 순환

3. 시스템 구조
상태 변수
- arr: 고정 크기 배열
- front: 삭제 위치
- rear: 삽입 위치
- size 또는 (rear + 1) % capacity == front로 full 판단

동작 원리
enqueue
- rear 위치에 삽입
- rear = (rear + 1) % capacity

dequeue
- front 위치에서 제거
- front = (front + 1) % capacity
→ 이동 없이 포인터만 변경 → O(1)

4. 데이터 흐름
초기:
[ _ _ _ _ _ ]
 front=0, rear=0

enqueue(1)
[ 1 _ _ _ _ ]
 front=0, rear=1

enqueue(2)
[ 1 2 _ _ _ ]
 front=0, rear=2

dequeue()
[ 1 2 _ _ _ ]
 front=1, rear=2  (1은 논리적으로 제거됨)

enqueue(3)
[ 1 2 3 _ _ ]
 front=1, rear=3

''' 
# 5. 구현 (Python)

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")

        self.arr[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")

        value = self.arr[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value
