# https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150

# gpt solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 1) 리스트를 절반으로 분할
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # type: ignore
            fast = fast.next.next

        mid = slow.next # type: ignore
        slow.next = None # type: ignore

        # 2) 각 절반 정렬
        left = self.sortList(head)
        right = self.sortList(mid) # type: ignore

        # 3) 정렬된 두 리스트 병합
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next # type: ignore
            else:
                tail.next = l2
                l2 = l2.next # type: ignore
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next

## 이하 테스트 케이스 생성용

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