#include <iostream>

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
    int depth = 0;
    void helper(TreeNode *node, int currentDepth) {
        if (node) {
            if (currentDepth > depth) depth = currentDepth;
            helper(node->left, currentDepth+1);
            helper(node->right, currentDepth+1);
        }
    }
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        helper(root, 1);
        return depth;
    }
};