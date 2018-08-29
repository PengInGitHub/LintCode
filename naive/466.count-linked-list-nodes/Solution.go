package nodes

func main() {

}

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * @param head: the first node of linked list.
 * @return: An integer
 */
func countNodes(head *ListNode) int {
	tmp := head
	count := 0
	for tmp != nil {
		count++
		tmp = tmp.Next
	}
	return count
}

func countNodesWorseEdition(head *ListNode) int {
	if head == nil {
		return 0
	}
	// write your code here
	count := 1
	for head.Next != nil {
		count++
		head.Next = head.Next.Next
	}
	return count
}
