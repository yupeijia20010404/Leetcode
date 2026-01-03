class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None and root.right != None:
            return self.maxDepth(root.right) + 1
        if root.left != None and root.right == None:
            return self.maxDepth(root.left) + 1
        if root.left != None and root.right != None:
            return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)