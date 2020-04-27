#include <iostream>
#include <vector>

using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return NULL;
        int len = lists.size();
        while (len > 1)
        {
            int halfLen = (len + 1) / 2;
            for(int i = 0; i < len / 2; ++i) {
                lists[i] = mergeTwoList(lists[i], lists[i+halfLen]);
            }
            len = halfLen;
        }
        return lists[0];
    }

    ListNode* mergeTwoList(ListNode* a, ListNode* b) {
        ListNode *dummy = new ListNode(-1);
        ListNode *rhead = dummy;
        while (a and b) {
            if (a->val <= b->val) {
                rhead->next = a;
                a = a->next;
            }else {
                rhead->next = b;
                b = b->next;
            }
            rhead = rhead->next;
        }
        rhead->next = a ? a : b;
        return dummy->next;
    }
};