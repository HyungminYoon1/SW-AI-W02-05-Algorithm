# https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    # 리스트 끝에 노드 추가
    def append(self, val):
        new_node = ListNode(val)

        if self.head == None:
            self.head = new_node
            return
        
        # 마지막 노드 찾기
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # 마지막 노드의 next를 new_node로 설정
        last_node.next = new_node
        return
    
    def print_list(self):
        """리스트의 모든 값 출력"""
        values = []
        
        # TODO: head부터 시작
        if self.head is None:
            values.append(self.head)
            return
        
        # TODO: 끝까지 순회하며 값 수집
        last= self.head
        while last:
            values.append(last.val)
            last = last.next
        
        return values

def sortList(LinkedList):
    
    last_node = LinkedList.head
    while last_node.next:
        last_node = last_node.next
        
    start_p = LinkedList.head
    end_p = last_node
    while start_p.next != last_node : # head부터 ~ 마지막까지
        pointer = LinkedList.head # 현재 위치: head부터 시작
        while pointer != end_p: # 현재 포인터가 마지막 포인터가 아니라면
            if pointer.val > pointer.next.val:
                pointer.val, pointer.next.val = pointer.next.val, pointer.val
            pointer = pointer.next # 현재 포인터 이동
        start_p = start_p.next

ll1 = LinkedList()
ll1.append(3)
ll1.append(4)
ll1.append(1)
ll1.append(2)

sortList(ll1)
print(ll1.print_list())

'''
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
'''