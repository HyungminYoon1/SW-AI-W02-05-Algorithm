# https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150

## 팀원 연습용 코드: 동작 실패
'''
class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, val):
        node = LinkNode(val)
        if self.tail is None:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head is None:
            raise IndexError('Queue is empty')
        val = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val
        
    def pyls_to_lkls(self, arr):
        if not arr:
            raise ValueError('Input list is empty')
        if self.head:
            raise RuntimeError('Queue must be empty to perform this operation')
        for val in arr:
            self.enqueue(val)


class Solution:
    def addTwoNumbers(self, l1, l2):
        text1 = ''
        text2 = ''

        list1 = []
        list2 = []
        while l1 != None:
            list1.append(l1.val)
            l1 = l1.next

        while l2 != None:
            list2.append(l2.val)
            l2 = l2.next

        l1 = list1
        l2 = list2

        

        while l1:
            text1 += str(l1.pop())

        while l2:
            text2 += str(l2.pop())

        result_rever_text = int(text1) + int(text2) # 정수
        result = str(result_rever_text)[::-1]

        print(list(map(int, result)))


l1 = [2,4,3]
l2 = [5,6,4]
lk_l1 = LinkedList()
lk_l2 = LinkedList()
lk_l1 = lk_l1.pyls_to_lkls(l1)
lk_l2 = lk_l2.pyls_to_lkls(l2)

Solution().addTwoNumbers(lk_l1, lk_l2)
'''

'''
# 테스트 케이스

tls = [1,2,3,4,5,6,7,8,9]
linked_list_test = LinkedList()
t = linked_list_test.pyls_to_lkls(tls)

print(t)

'''