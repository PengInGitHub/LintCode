package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/**
 * @param head: a ListNode
 * @param val: An integer
 * @return: a ListNode
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/**
 * @param head: a ListNode
 * @param val: An integer
 * @return: a ListNode
 */
func removeElements(head *ListNode, val int) *ListNode {
	// write your code here
	//made-up header for head
	dummy := &ListNode{Val: 0}
	dummy.Next = head
	head = dummy
	for head.Next != nil {
		if head.Next.Val == val {
			head.Next = head.Next.Next
		} else {
			head = head.Next
		}
	}
	return dummy.Next
}
