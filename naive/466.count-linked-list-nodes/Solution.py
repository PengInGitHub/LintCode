"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNode(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count
    

    
    def countNodes(self, head):
        # write your code here
        tmp = head
        count = 0
        while (tmp):
            count += 1
            tmp = tmp.next
        return count
    