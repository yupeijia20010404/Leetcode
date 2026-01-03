class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None:
            return q == None
        if q == None:
            return p == None
        if p.left == None:
            if q.left != None:
                return False
            if p.right == None:
                if q.left == None and q.right == None:
                    if p.val == q.val:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return self.isSameTree(p.right, q.right) and p.right.val == q.right.val
        elif p.right == None:
            if q.right != None:
                return False
            if p.left == None:
                if q.left == None and q.right == None:
                    if p.val == q.val:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return self.isSameTree(p.left, q.left) and p.left.val == q.left.val
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)