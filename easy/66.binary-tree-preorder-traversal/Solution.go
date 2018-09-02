/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

/**
 * @param root: A Tree
 * @return: Preorder in ArrayList which contains node values.
 */

var res = make([]int, 0)

func preorderTraversal(root *TreeNode) []int {
	// write your code here
	return dfs(root, res)
}

func dfs(root *TreeNode, res []int) []int {
	if root != nil {
		res = append(res, root.Val)
		dfs(root.Left, res)
		dfs(root.Right, res)
	}
	return res
}

func preorderTraversal2(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	res := []int{root.Val}
	left := preorderTraversal(root.Left)
	right := preorderTraversal(root.Right)
	res = append(res, left...)
	res = append(res, right...)
	return res
}

func preorderTraversal3(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	res = append(res, root.Val)
	preorderTraversal(root.Left)
	preorderTraversal(root.Right)
	return res
}
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 