"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        # write your code here
        if root == None:
            return root
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max_node(root, self.max_node(left, right))
    
    def max_node(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        if left.val>right.val:
            return left
        return right
        
