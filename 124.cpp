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
    int maxSum = INT_MIN;
    int pathSum(TreeNode* root) {
        if (root==nullptr) return 0;

        int r = pathSum(root->right);
        int l = pathSum(root->left);
        
        int currentMaxSum = l > 0 ? root->val + l + (r > 0 ? r : 0) : root->val + (r > 0 ? r : 0);
        if (currentMaxSum > maxSum) maxSum = currentMaxSum;
        
        return root->val + max(0, max(l, r)); //只能选左右子树中的一个或者不选
    }
public:
    int maxPathSum(TreeNode* root) {
        if (root==nullptr) return 0;
        pathSum(root);
        return maxSum;
    }
};