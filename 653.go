package leetcode

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findTarget(root *TreeNode, k int) bool {
	left, right := root, root
	// left指向最小元素, right指向最大元素
	left_stack, right_stack := []*TreeNode{left}, []*TreeNode{right}

	for left.Left != nil {
		left = left.Left
		left_stack = append(left_stack, left)
	}

	for right.Right != nil {
		right = right.Right
		right_stack = append(right_stack, right)
	}

	for left != right {
		if tmp := left.Val + right.Val; tmp == k {
			return true
		} else if tmp < k {
			left_stack = left_stack[:len(left_stack)-1]
			node := left.Right
			for node != nil {
				left_stack = append(left_stack, node)
				node = node.Left
			}
			left = left_stack[len(left_stack)-1]
		} else {
			right_stack = right_stack[:len(right_stack)-1]
			node := right.Left
			for node != nil {
				right_stack = append(right_stack, node)
				node = node.Right
			}
			right = right_stack[len(right_stack)-1]
		}
	}
	return false
}
