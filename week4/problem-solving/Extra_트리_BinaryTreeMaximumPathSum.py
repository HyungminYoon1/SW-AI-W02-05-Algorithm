# 트리 - Binary Tree Maximum Path Sum
# 문제 링크: https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150

'''
풀이 전략

이 문제의 핵심은 한 노드에서 두 가지 값을 다르게 생각하는 것입니다.

1. 부모에게 넘길 값
부모는 현재 노드에서 한쪽 방향만 이어 받을 수 있습니다.
그래서 left + node + right를 부모에게 넘기면 안 됩니다.
부모에게 반환하는 값은: node.val + max(left_gain, right_gain)

2. 현재 노드를 "가운데"로 쓰는 경로 값
최대 경로합 후보는 현재 노드에서 왼쪽과 오른쪽을 둘 다 사용할 수 있습니다.
즉, 현재 노드 기준 후보는: node.val + left_gain + right_gain
이 값으로 전체 최댓값을 계속 갱신합니다.

*가장 중요한 힌트:
dfs(node)는 "이 노드에서 시작해서 부모 쪽으로 올려보낼 수 있는 최대 합"을 반환하세요.
동시에 바깥 변수 하나(answer)를 두고, 각 노드마다 node.val + left_gain + right_gain 로 갱신
어떤 자식 경로가 음수면 차라리 안 쓰는 게 낫습니다.

'''

'''
Input: root = [1,2,3]
Output: 6
'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]):

        answer = float('-inf')

        def dfs(node):

            nonlocal answer

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            answer = max(answer, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)
        
        return answer