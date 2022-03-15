package leetcode

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	var ans *TreeNode
	var dfs func(*TreeNode) (bool, bool)
	dfs = func(node *TreeNode) (hasP, hasQ bool) {
		if node == nil || ans != nil {
			return
		}
		lP, lQ := dfs(node.Left)
		rP, rQ := dfs(node.Right)
		if node == p || lP || rP {
			hasP = true
		}
		if node == q || lQ || rQ {
			hasQ = true
		}
		if hasP && hasQ {
			if ans == nil {
				ans = node
			}
		}
		return hasP, hasQ
	}

	dfs(root)
	return ans
}
