package leetcode

/*
 * @lc app=leetcode.cn id=160 lang=golang
 *
 * [160] 相交链表
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	a, b := headA, headB
	for a != nil && b != nil {
		if a == b {
			return a
		}
		a = a.Next
		b = b.Next
	}
	if a == nil {
		headA, headB = headB, headA
		a, b = b, a
	}
	for a != nil {
		a = a.Next
		headA = headA.Next
	}
	for headA != nil {
		if headA == headB {
			return headA
		}
		headA = headA.Next
		headB = headB.Next
	}
	return nil
}

// @lc code=end
