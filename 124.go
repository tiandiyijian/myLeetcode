package leetcode

import "math"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxPathSum(root *TreeNode) int {
	ans := math.MinInt

	var dfs func(root *TreeNode) int
	dfs = func(root *TreeNode) int {
		if root == nil {
			return 0
		}

		maxSon := 0
		left := dfs(root.Left)
		maxSon = max(maxSon, left)

		right := dfs(root.Right)
		maxSon = max(maxSon, right)

		cur := root.Val
		// ans = max(ans, maxSon) //不需要考虑这种情况，因为子节点已经考虑过了
		ans = max(ans, cur+maxSon)
		ans = max(ans, cur+left+right)

		return cur + maxSon
	}

	dfs(root)
	return ans
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
