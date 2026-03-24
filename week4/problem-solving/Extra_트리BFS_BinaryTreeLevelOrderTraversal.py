# 트리, BFS - Binary Tree Level Order Traversal
# 문제 링크: https://leetcode.com/problems/binary-tree-level-order-traversal/

'''
풀이 전략

이 문제의 핵심 힌트는 “같은 깊이에 있는 노드들을 한 번에 모아야 한다”는 점입니다. 
그래서 DFS보다 BFS(너비 우선 탐색)가 더 자연스럽습니다.

1. queue에 현재 방문할 노드들을 넣습니다.
2. 처음에는 root 하나만 넣고 시작합니다.
3. while queue:를 돌리되, 매 반복마다 현재 queue 길이를 먼저 저장합니다.
4. 그 길이만큼만 꺼내면, 그 노드들은 모두 “같은 레벨”의 노드들입니다.
5. 그 레벨의 값들을 리스트에 모으고, 각 노드의 left, right를 다음 레벨 탐색용으로 queue에 넣습니다.
6. 한 레벨 처리가 끝날 때마다 결과 배열에 추가합니다.

queue를 끝까지 다 비우면 안 되고, “이번 레벨의 개수만큼만” 처리해야 레벨별로 묶을 수 있습니다.
root is None인 경우를 먼저 처리해야 합니다.
레벨마다 임시 리스트 level = []를 만들어 값을 담으면 구조가 깔끔합니다.

'''
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
# 입력 예제
root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)
# 기대 출력: [[3],[9,20],[15,7]]
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        
        if not root:
            return []

        result_list = [] # 결과를 담는 리스트

        q = deque([root])
        level_size = 0 # 해당 레벨에서 갖는 큐 사이즈

        while q:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)

                # 자식 노드가 있으면 다음 작업 큐로 이동
                if node.left:
                    q.append(node.left) 
                
                if node.right:
                    q.append(node.right)
        
            result_list.append(level) # 현재 레벨 처리 종료
            
        return result_list
'''
sol = Solution()
print(sol.levelOrder(root))
'''