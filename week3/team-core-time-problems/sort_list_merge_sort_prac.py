class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode: # type: ignore
        if not head or not head.next:
            return head

        # 머지 정렬 함수 구현하세요~~
        '''
        연결 리스트에서 가운데 찾기: slow, fast 포인터를 씁니다.
        slow는 한 칸씩, fast는 두 칸씩 이동
        fast가 끝에 도달했을 때 slow는 중간 근처에 있습니다.
        '''

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next
        
        # 리스트를 중간에서 끊기
        mid = slow.next # type: ignore
        slow.next = None # type: ignore

        # 각 절반 정렬
        left = self.sortList(head)
        right = self.sortList(mid) # type: ignore

        # 3) 정렬된 두 리스트 병합
        return self.merge(left, right)
        
    '''
    연결 리스트에서 merge 하는 방법: 값을 교환하는 게 아니라, 작은 노드를 골라서 next로 이어 붙입니다.
    예) l1: 1 -> 4 -> 5
        l2: 2 -> 3 -> 6
        => 1과 2 비교 => 2와 4 비교 => 3과 4 비교 => 4와 5 비교 => 5와 6 비교
        => 1 2 3 4 5 6 순으로 정렬
    '''
    def merge(self, l1: ListNode, l2: ListNode):
        dummy = ListNode() # dummy는 시작점 역할
        tail = dummy # tail은 현재까지 만든 정렬 리스트의 마지막 노드

        while l1 and l2: # l1, l2 중 하나라도 끝에 도달해서 next 가 None 이 되면 while문 탈출
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next # type: ignore
            else:
                tail.next = l2
                l2 = l2.next # type: ignore
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next

'''
테스트 케이스 생성 및 출력용
'''

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result

test_cases = [
    [],
    [1],
    [4, 2, 1, 3],
    [-1, 5, 3, 4, 0],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [2, 2, 1, 1],
    [5, -2, 3, 0, -1],
]

solution = Solution()

for i, case in enumerate(test_cases, 1):
    head = build_linked_list(case)
    sorted_head = solution.sortList(head) # type: ignore
    result = linked_list_to_list(sorted_head)
    expected = sorted(case)

    print(f"Test {i}")
    print("input   :", case)
    print("result  :", result)
    print("expected:", expected)
    print("pass    :", result == expected)
    print()