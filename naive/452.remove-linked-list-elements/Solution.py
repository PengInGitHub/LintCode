"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
#https://www.jiuzhang.com/solution/remove-linked-list-elements/

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        #head needs a pre-node 
        dummy = ListNode(0)
        dummy.next = head
        #update head, now it has a pre-node
        head = dummy
        #head.next = original head
        while head.next != None:
            if head.next.val == val:
                #remove
                head.next = head.next.next
            else:
                head = head.next
        #return head is wrong here
        #b/c head has the first made-up header with value of zero
        #if should start from head.next
        #should not return head, becasue head is always changing, only sub of original
        #return head.next
        return dummy.next