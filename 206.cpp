#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        return nullptr;
    }
};

ListNode* change_node(ListNode* node) {
    cout << node << endl;
    node->val = 3;
    node = (node->next);
    node->val = 4;
    return node;
}

int main(int argc, char const *argv[])
{
    // ListNode* a = new ListNode(1);
    // ListNode* b = new ListNode(2);
    ListNode a(1), b(2);
    a.next = &b;
    ListNode c = a;
    
    cout << "a: " << &a << " b: " << &b << " c: " << &c << endl;
    auto d = change_node(&a);
    cout << "d: " << &d << endl;
    cout << a.val << b.val <<  d->val <<endl;
    // cout << a.val << b.val << change_node(a).val << a.val << endl;
    int num = 1;
    int* add = &num;
    cout << add << " " << *add << endl;
    cout << &add << endl;
    cout << &num;
    return 0;
}
