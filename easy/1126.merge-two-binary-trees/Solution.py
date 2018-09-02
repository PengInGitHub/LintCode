"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def mergeTrees1(self, t1, t2):
        # Write your code here
        if t1 is None and t2 is None:
            return
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        else:
            node = TreeNode(t1.val+t2.val)
            left = self.mergeTrees(t1.left, t2.left)
            right = self.mergeTrees(t1.right, t2.right)
            node.left, node.right = left, right
        return node

    def mergeTrees(self, t1, t2):
        #set t1 as the main tree, t2 the sub tree
        #aka transfer the value of t2 to t1
        
        #both not none
        if t1 is not None and t2 is not None:
            #update value
            t1.val += t2.val
            #update left and right child of t1
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            #return new t1
            return t1
        
        return t1 if t2 is None else t2
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
