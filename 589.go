package leetcode

// Definition for a Node.
type Node struct {
	Val      int
	Children []*Node
}

func preorder1(root *Node) []int {
	ans := []int{}
	if root == nil {
		return ans
	}

	var helper func(node *Node)
	helper = func(node *Node) {
		if node == nil {
			return
		}
		ans = append(ans, node.Val)
		for _, child := range node.Children {
			helper(child)
		}
	}

	helper(root)
	return ans
}

func preorder(root *Node) []int {
	ans := []int{}
	if root == nil {
		return ans
	}
	q := []*Node{root}
	for len(q) > 0 {
		node := q[0]
		q = q[1:]
		ans = append(ans, node.Val)
		// q = append(q, node.Children...)
		// 不正经反着来了属于是
		q = append(node.Children, q...)
	}
	return ans
}

func preorder2(root *Node) []int {
	ans := []int{}
	if root == nil {
		return ans
	}
	s := []*Node{root}
	for len(s) > 0 {
		node := s[len(s)-1]
		s = s[:len(s)-1]
		ans = append(ans, node.Val)
		for i := len(node.Children) - 1; i >= 0; i-- {
			s = append(s, node.Children[i])
		}
	}
	return ans
}
