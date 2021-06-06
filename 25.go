package main

import "fmt"

/*
 * @lc app=leetcode.cn id=25 lang=golang
 *
 * [25] K 个一组翻转链表
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
func reverseK(node *ListNode, k int) (head *ListNode, tail *ListNode, next *ListNode) {
	if node == nil {
		return
	}
	n := 0
	tmpNode := node
	for tmpNode != nil {
		n++
		tmpNode = tmpNode.Next
	}
	if n < k {
		return node, nil, nil
	}
	tail = node
	a, b := node, node.Next
	node.Next = nil //防止循环引用
	for i := 0; i < k-1; i++ {
		tmp := b.Next
		b.Next = a
		a, b = b, tmp
	}
	head = a
	next = b
	return
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{}
	preTail := dummy
	next := head
	var groupHead, groupTail *ListNode
	for next != nil {
		groupHead, groupTail, next = reverseK(next, k)
		preTail.Next = groupHead
		if groupTail == nil {
			return dummy.Next
		}
		preTail = groupTail
	}
	return dummy.Next
}

// @lc code=end

func main() {
	head := &ListNode{1, &ListNode{2, nil}}
	ans := reverseKGroup(head, 2)
	fmt.Println(ans.Val, ans.Next.Val)
}
