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
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val > q->val) swap(p, q);
        if(root->val < p->val){          //p和q都在右子树上
            return lowestCommonAncestor(root->right, p, q);
        }else if(root->val > q->val) {   //p和q都在左子树上
            return lowestCommonAncestor(root->left, p, q);
        }
        return root;        
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p->val > q->val) swap(p, q);
        TreeNode* node = root;
        while (node) {
            if(node->val < p->val){          //p和q都在右子树上
                node = node->right;
            }else if(node->val > q->val) {   //p和q都在左子树上
                node = node->left;
            }else {
                return node;
            }    
        }
        return nullptr;        
    }
};

int main(int argc, char const *argv[])
{
    cout << 0;
    return 0;
}
