package leetcode

import "strconv"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func tree2str(root *TreeNode) string {
	if root == nil {
		return ""
	}

	ans := strconv.Itoa(root.Val)
	left := tree2str(root.Left)
	right := tree2str(root.Right)

	if len(left) == 0 && len(right) == 0 {
		return ans
	} else if len(left) == 0 {
		return ans + "(()" + "(" + right + "))"
	} else if len(right) == 0 {
		return ans + "(" + left + ")"
	} else {
		return ans + "((" + left + ")" + "(" + right + "))"
	}
}
