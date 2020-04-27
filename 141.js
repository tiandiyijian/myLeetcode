var ListNode = /** @class */ (function () {
    function ListNode(val) {
        this.val = val;
    }
    return ListNode;
}());
var hasCycle = function (head) {
    if (head === null || head.next === null)
        return false;
    var slow = head;
    var fast = head.next;
    while (slow !== fast) {
        if (fast == null || fast.next == null)
            return false;
        slow = slow.next;
        fast = fast.next;
        fast = fast.next;
    }
    return true;
};
