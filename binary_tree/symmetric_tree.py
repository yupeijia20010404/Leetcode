# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isLeafSymmetric(left, right) -> bool:
            if left.left == None and left.right == None and right.left == None and right.right == None:
                return True
            if left.left != None:
                if right.right == None:
                    return False
                else:
                    if right.right.val != left.left.val:
                        return False
            else:
                if right.right != None:
                    return False
            if left.right != None:
                if right.left == None:
                    return False
                else:
                    if left.right.val != right.left.val:
                        return False
            else:
                if right.left != None:
                    return False
            res = True
            if left.left != None and right.right != None:
                res = res and isLeafSymmetric(left.left, right.right)
            if left.right != None and right.left != None:
                res = res and isLeafSymmetric(left.right, right.left)
            return res

        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False
        if root.left.val != root.right.val:
            return False
        
        return isLeafSymmetric(root.left, root.right)