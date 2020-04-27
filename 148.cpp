#include <iostream>
#include <utility>

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
    ListNode* sortList(ListNode* head) {
        int len = 0;
        ListNode* tmp = head;
        while (tmp)
        {
            tmp = tmp->next;
            ++len;
        }
        ListNode dummy(-1);
        dummy.next = head;
        for (int i = 1; i < len; i *= 2)
        {
            ListNode* cur = dummy.next;
            ListNode* tail = &dummy;
            while (cur) {
                auto l = cur;
                auto r = split(cur, i);
                cur = split(r, i);
                auto nodes = merge(l, r);
                tail->next = nodes.first;
                tail = nodes.second;
            }
        }
        return dummy.next;
    }

private:
    pair<ListNode*, ListNode*> merge(ListNode* a, ListNode* b) {
        ListNode dummy(-1);
        ListNode *tail = &dummy;
        while (a && b) {
            if (a->val <= b->val) {
                tail->next = a;
                a = a->next;
            }else {
                tail->next = b;
                b = b->next;
            }
            tail = tail->next;
        }
        tail->next = a ? a : b;
        while (tail->next) tail = tail->next;
        return make_pair(dummy.next, tail);
    }

    ListNode* split(ListNode* a, int len) {
        while (len > 1 && a) {
            a = a->next;
            --len;
        }
        ListNode* rest = a ? a->next : nullptr; //有可能从a到结尾不到len个节点，此时a为空
        if (a) a->next = nullptr; //断开左右两部分
        return rest;
    }
};