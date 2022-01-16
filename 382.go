package leetcode

import "math/rand"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type Solution struct {
	head *ListNode
}

func Constructor(head *ListNode) Solution {
	return Solution{
		head,
	}
}

func (this *Solution) GetRandom() int {
	ans := 0
	head := this.head
	for i := 0; head != nil; i++ {
		if rand.Intn(i+1) == 0 { // 1/i的概率被选中
			ans = head.Val
		}
		head = head.Next
	}
	return ans
}

/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
