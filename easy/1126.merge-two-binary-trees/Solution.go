/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param t1: the root of the first tree
 * @param t2: the root of the second tree
 * @return: the new binary tree after merge
 */
func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	// Write your code here
	//choose t1 as the main node
	//this means that, if both of t1 and t2 exist, attach the value of t2 to t1
	//remain t1 and ignore t2
	//if not all of them exist, return t1 by default, if t1 not exist, return t2
	if t1 != nil && t2 != nil {
		//update value
		t1.Val += t2.Val
		//update left child
		t1.Left = mergeTrees(t1.Left, t2.Left)
		//update right child
		t1.Right = mergeTrees(t1.Right, t2.Right)
		//return updated t1
		return t1
	}
	if t2 == nil {
		return t1
	}
	return t2
}
