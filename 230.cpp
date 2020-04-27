#include <iostream>
#include <vector>

using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    int ans, count = 0;
    void inOrder(TreeNode* node, int &k) {
        if (!node) return;
        // cout << node->val << endl;
        inOrder(node->left, k);
        if (count >= k) return;
        ++count;
        if(count == k) {
            ans = node->val;
            return;
        }
        inOrder(node->right, k);
    }
public:
    int kthSmallest(TreeNode* root, int k) {
        inOrder(root, k);
        // cout << nums.size();
        return ans;
    }
};