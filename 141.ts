class ListNode {
    val: number;
    next: null;
    constructor(val: number) {
        this.val = val;
    }
}

let hasCycle = function(head: ListNode):boolean {
    if (head === null || head.next === null) return false;
    let slow: ListNode = head;
    let fast: ListNode = head.next;
    while (slow !== fast) {
        if (fast == null || fast.next == null) return false;
        slow = slow.next;
        fast = fast.next;
        fast = fast.next;
    }
    return true;
}