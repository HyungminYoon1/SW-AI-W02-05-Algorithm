from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result_list = []
        max_level = self.maxDepth(root)

        for level in range(1, max_level + 1):
            level_sum = self.sumOfLevels(root, level)
            node_count = self.childCounts(root, level)
            result_list.append(level_sum / node_count)

        return result_list

    def sumOfLevels(self, root: Optional[TreeNode], level: int) -> int:
        if not root:
            return 0

        if level == 1:
            return root.val

        left_sum = self.sumOfLevels(root.left, level - 1)
        right_sum = self.sumOfLevels(root.right, level - 1)

        return left_sum + right_sum

    def childCounts(self, root: Optional[TreeNode], level: int) -> int:
        if not root:
            return 0

        if level == 1:
            return 1

        left_count = self.childCounts(root.left, level - 1)
        right_count = self.childCounts(root.right, level - 1)

        return left_count + right_count
