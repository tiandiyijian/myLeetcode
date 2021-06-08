package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
	dummy := &ListNode{Next: head}
	cur := head
	pre := dummy
	for cur != nil {
		if cur.Val == val {
			pre.Next = cur.Next
			cur = cur.Next
		} else {
			pre = pre.Next
			cur = cur.Next
		}
	}
	return dummy.Next
}
