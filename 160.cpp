#include <iostream>

using namespace std;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) return nullptr;
        auto nodeA = headA, nodeB = headB;
        while (nodeA->next || nodeB->next) {
            if (nodeA == nodeB) return nodeA;
            // cout << nodeA->val << nodeB->val << endl;
            nodeA = nodeA->next ? nodeA->next : headB;
            nodeB = nodeB->next ? nodeB->next : headA;
        }
        return nodeA == nodeB ? nodeA : nullptr;
    }


    ListNode *getIntersectionNode1(ListNode *headA, ListNode *headB) {
        auto nodeA = headA, nodeB = headB;
        int lenA = 0, lenB = 0;
        while (nodeA && nodeB) {
            ++lenA;
            ++lenB;
            nodeA = nodeA->next;
            nodeB = nodeB->next;
        }
        int diff = 0;
        while (nodeA) {
            ++diff;
            nodeA = nodeA->next;
        }
        while (nodeB) {
            ++diff;
            nodeB = nodeB->next;
        }
        nodeA = headA;
        nodeB = headB;
        if (lenA > lenB) {
            while (diff)
            {
                --diff;
                nodeA = nodeA->next;
            }
        }else
        {
            while (diff)
            {
                --diff;
                nodeB = nodeB->next;
            }
        }
        while (nodeA && nodeB)
        {
            if (nodeA == nodeB) return nodeA;
            nodeA = nodeA->next;
            nodeB = nodeB->next;
        }
        return nullptr;
    }
};