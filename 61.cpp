/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
  		if(head == NULL) return head;
  		int len = 0;
  		auto thead = head;
  		while(thead -> next) {
  			thead = thead -> next;
  			++len;
  		}
  		++len;
  		int num = k % len;
  		if(num == 0) return head;
  		int tar = len - num;
  		cout << tar << " " << num;
  		auto t = head;
  		while(--tar) {
  			t = t -> next;
  		}
  		auto newHead = t -> next;
  		t -> next = NULL;
  		thead -> next = head;
  		head = newHead;
  		return head;
    }
};