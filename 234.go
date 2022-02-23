package leetcode

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
	slow := head
	fast := head
	var pre *ListNode
	for fast != nil && fast.Next != nil {
		fast = fast.Next.Next
		next := slow.Next
		slow.Next = pre
		pre = slow
		slow = next
	}

	behind := slow
	front := pre
	pre = slow
	if fast != nil {
		behind = slow.Next
	}
	for front != nil {
		if front.Val != behind.Val {
			return false
		}
		frontNext := front.Next
		front.Next = pre
		pre = front
		front = frontNext
		behind = behind.Next
	}

	// for head != nil {
	//     fmt.Println(head.Val)
	//     head = head.Next
	// }
	return true
}
