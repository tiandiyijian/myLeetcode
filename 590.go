package leetcode

//  Definition for a Node.
type Node struct {
	Val      int
	Children []*Node
}

func postorder(root *Node) []int {
	ans := []int{}
	if root == nil {
		return ans
	}

	stack := []*Node{root}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		ans = append(ans, node.Val)
		stack = append(stack, node.Children...)
	}

	for i, j := 0, len(ans)-1; i < j; i++ {
		ans[i], ans[j] = ans[j], ans[i]
		j--
	}

	return ans
}

func postorder2(root *Node) (ans []int) {
	if root == nil {
		return
	}
	stack := []interface{}{root}
	for l := len(stack); l > 0; l = len(stack) {
		obj := stack[l-1]
		stack = stack[:l-1]
		if value, ok := obj.(int); ok {
			ans = append(ans, value)
		} else {
			value, _ := obj.(*Node)
			stack = append(stack, value.Val)
			// 这个写法有点秀
			// 对于一个节点存在未访问、访问了但还没访问子节点、访问完子节点又访问三种状态
			// 在第三种状态的时候才可以把节点值放到答案里
			// 别的做法都是专门添加一个变量表示中间状态
			// 比如{node, isVisited}这种
			// 但是这种做法就很妙，直接把节点值当作中间状态
			for i := len(value.Children) - 1; i >= 0; i-- {
				stack = append(stack, value.Children[i])
			}
		}
	}
	return
}
