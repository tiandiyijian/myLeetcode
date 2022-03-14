package leetcode

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func postorderTraversal(root *TreeNode) (ans []int) {
	if root == nil {
		return
	}

	stack := []*TreeNode{root}
	gotoHLVFL := func() {
		// 左侧最高可见节点
		// highest leaf visible from left
		for node := stack[len(stack)-1]; node != nil; node = stack[len(stack)-1] {
			if node.Left != nil {
				// 尽可能向左
				if node.Right != nil {
					stack = append(stack, node.Right)
				}
				stack = append(stack, node.Left)
			} else {
				// 实不得已才向右
				stack = append(stack, node.Right)
			}
		}
		stack = stack[:len(stack)-1]
	}

	for len(stack) > 0 {
		if stack[len(stack)-1].Left != root && stack[len(stack)-1].Right != root {
			// 如果当前栈顶节点不是其父，那就是其右兄
			// 找到其右兄为根的子树中的HLVFL(相当于递归深入其中)
			gotoHLVFL()
		}
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		ans = append(ans, root.Val)
	}

	return
}
