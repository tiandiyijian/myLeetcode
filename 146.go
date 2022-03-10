package leetcode

type Node struct {
	Key  int
	Val  int
	Prev *Node
	Next *Node
}

type List struct {
	Head *Node
	Tail *Node
	Size int
}

func (list *List) Add(node *Node) {
	if list.Size == 0 {
		list.Head = node
		list.Tail = node
	} else if list.Size == 1 {
		list.Tail = node
		list.Head.Next = list.Tail
		list.Tail.Prev = list.Head
	} else {
		list.Tail.Next = node
		node.Prev = list.Tail
		list.Tail = node
	}
	list.Size++
}

func (list *List) Move2End(node *Node) {
	if list.Size <= 1 {
		return
	}
	if list.Tail == node {
		return
	}
	prev, next := node.Prev, node.Next
	if prev == nil {
		list.Head = next
		next.Prev = nil
		node.Next = nil
		node.Prev = list.Tail
		list.Tail.Next = node
		list.Tail = node
		return
	}
	prev.Next, next.Prev = next, prev
	list.Tail.Next = node
	node.Prev = list.Tail
	node.Next = nil
	list.Tail = node
}

type LRUCache struct {
	capacity int
	data     map[int]*Node
	list     *List
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		data:     map[int]*Node{},
		list:     &List{},
	}
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.data[key]; ok {
		this.list.Move2End(node)
		return node.Val
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.data[key]; ok {
		node.Val = value
		this.list.Move2End(node)
		return
	}
	if len(this.data) == this.capacity {
		head := this.list.Head
		this.list.Move2End(head)
		// fmt.Println(this.data)
		delete(this.data, head.Key)
		this.data[key] = head
		// fmt.Println(this.data)
		head.Key = key
		head.Val = value
		return
	}
	node := &Node{
		Key: key,
		Val: value,
	}
	this.data[key] = node
	this.list.Add(node)
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */

// func main() {
// 	lRUCache := Constructor(2)
// 	lRUCache.Put(1, 1)
// 	lRUCache.Put(2, 2)
// 	fmt.Println(lRUCache.Get(1))
// 	lRUCache.Put(3, 3)
// 	fmt.Println(lRUCache.Get(2))
// }
