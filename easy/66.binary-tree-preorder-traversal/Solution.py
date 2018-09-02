"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def __init__(self):
        self.res = []
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal1(self, root):
        # write your code here
        if root:
            self.res.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.res
        
    def preorderTraversal2(self, root):
        res = []
        def dfs(root):
            if root:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
            return res
        return dfs(root)
    
    def preorderTraversal(self, root):
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
