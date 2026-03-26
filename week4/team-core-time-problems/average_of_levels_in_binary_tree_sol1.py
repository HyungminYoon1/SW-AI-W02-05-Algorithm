
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def solve(self, nodes): # nodes: 해당 레벨의 모든 노드
        level_avg = 0 # 해당 레벨의 평균값
        cnt = len(nodes) # 해당 레벨의 노드 숫자
        if cnt == 0 or not nodes: 
            return [] 

        next_nodes = []
        for node in nodes:
            level_avg += node.val
            if node.left : next_nodes.append(node.left)
            if node.right: next_nodes.append(node.right)
        
        ret = level_avg / cnt # 해당 레벨의 평균
        ret_list = [ret]

        ret_list.extend(self.solve(next_nodes)) # 다음 레벨로 확장

        return ret_list
        
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        return self.solve([root])