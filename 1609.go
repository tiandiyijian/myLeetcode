package leetcode

import "math"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isEvenOddTree(root *TreeNode) bool {
	// ans = true
	level := 0
	q := []*TreeNode{root}
	for len(q) > 0 {
		// fmt.Println(q)
		// tmp := len(q)
		// pre := q[0]
		// if !judgeVal(pre, level) {
		//     return false
		// }
		// new_q := []*TreeNode{}
		// if pre.Left != nil {
		//     new_q = append(new_q, pre.Left)
		// }
		// if pre.Right != nil {
		//     new_q = append(new_q, pre.Right)
		// }
		pre := new(TreeNode)
		if level == 0 {
			pre.Val = math.MinInt32
		} else {
			pre.Val = math.MaxInt32
		}
		new_q := []*TreeNode{}
		for i := 0; i < len(q); i++ {
			cur := q[i]
			if !(judgeVal(cur, level) && judgeOrder(pre, cur, level)) {
				return false
			}
			pre = cur
			if pre.Left != nil {
				new_q = append(new_q, pre.Left)
			}
			if pre.Right != nil {
				new_q = append(new_q, pre.Right)
			}
		}
		q = new_q
		level = 1 - level
	}
	return true
}

func judgeVal(node *TreeNode, level int) bool {
	return (level == 0 && node.Val&1 == 1) || (level == 1 && node.Val&1 == 0)
}

func judgeOrder(a, b *TreeNode, level int) bool {
	if level == 0 {
		return a.Val < b.Val
	}
	return a.Val > b.Val
}
