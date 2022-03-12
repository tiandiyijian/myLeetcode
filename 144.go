package leetcode

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorderTraversal(root *TreeNode) (ans []int) {
	if root == nil {
		return
	}

	stack := []*TreeNode{root}
	for l := len(stack); l > 0; l = len(stack) {
		node := stack[l-1]
		stack = stack[:l-1]
		ans = append(ans, node.Val)
		if node.Right != nil {
			stack = append(stack, node.Right)
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
		}
	}

	return
}
