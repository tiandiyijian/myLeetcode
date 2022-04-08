package leetcode

// Definition for a Node.
type Node struct {
	Val      int
	Children []*Node
}

func levelOrder(root *Node) [][]int {
	ans := [][]int{}
	if root == nil {
		return ans
	}
	q := []*Node{root}
	ans = append(ans, []int{root.Val})
	for len(q) > 0 {
		new_q := []*Node{}
		cur_level := []int{}
		for _, node := range q {
			for _, child := range node.Children {
				new_q = append(new_q, child)
				cur_level = append(cur_level, child.Val)
			}
		}
		q = new_q
		ans = append(ans, cur_level)
	}
	return ans[:len(ans)-1]
}
