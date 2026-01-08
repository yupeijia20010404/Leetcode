# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        nodes = []
        while len(queue) > 0:
            num_of_nodes = len(queue)
            for i in range(num_of_nodes):
                curr = queue.pop(0)
                nodes.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        ascend_nodes = sorted(nodes)
        return min([ascend_nodes[i + 1] - ascend_nodes[i] for i in range(len(ascend_nodes) - 1)])