# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        ans = []
        while len(queue) > 0:
            row_sum = 0
            row_count = len(queue)
            for i in range(row_count):
                curr = queue.pop(0)
                row_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(row_sum / row_count)
        return ans