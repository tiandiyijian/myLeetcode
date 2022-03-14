package leetcode

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal2(root *TreeNode) (ans []int) {
	if root == nil {
		return
	}
	stack := []interface{}{root}
	for l := len(stack); l > 0; l = len(stack) {
		node := stack[l-1]
		stack = stack[:l-1]
		if val, ok := node.(int); ok {
			ans = append(ans, val)
		} else {
			treeNode, _ := node.(*TreeNode)
			if treeNode.Right != nil {
				stack = append(stack, treeNode.Right)
			}
			stack = append(stack, treeNode.Val)
			if treeNode.Left != nil {
				stack = append(stack, treeNode.Left)
			}
		}
	}
	return ans
}

func inorderTraversal(root *TreeNode) (ans []int) {
	if root == nil {
		return
	}
	stack := []*TreeNode{}

	goLeft := func(root *TreeNode) {
		// 有了这个东西出栈的节点都可以直接把值加到ans中
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
	}

	goLeft(root)

	for l := len(stack); l > 0; l = len(stack) {
		node := stack[l-1]
		stack = stack[:l-1]
		ans = append(ans, node.Val)
		goLeft(node.Right)
	}

	return ans
}
