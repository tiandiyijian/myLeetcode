#include <vector>
#include <iostream>

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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.empty() || postorder.empty()) return nullptr;
        else return constructBinTree(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
    }

private:
    TreeNode* constructBinTree(vector<int> &inorder, int startInorder,
        int endInorder, vector<int> &postorder, int startPostorder, int endPostorder) {
            cout << "endPostorder: " << endPostorder << " ";
            if (startInorder > endInorder || startPostorder > endPostorder) return nullptr;
            int rootValue = postorder[endPostorder];
            cout << rootValue;
            TreeNode *root = new TreeNode(rootValue);
            // if (startInorder == endInorder) {
            //     if (startPostorder == endPostorder && inorder[startInorder] == postorder[startPostorder]) {
            //         cout << "equal\n";
            //         return root;
            //     }
            // }
            
            int rootInorder = startInorder;
            while (rootInorder <= endInorder && inorder[rootInorder] != rootValue)
            {
                ++rootInorder;
            }
            
            int num = rootInorder - startInorder;
            cout << " " << rootInorder << " " << num << endl;

            root->left = constructBinTree(inorder, startInorder, rootInorder - 1, postorder, startPostorder, startPostorder + num -1);
            root->right = constructBinTree(inorder, rootInorder + 1, endInorder, postorder, startPostorder + num, endPostorder-1);
            return root;
        }
};

int main(int argc, char const *argv[])
{
    vector<int> inorder({1, 2});
    vector<int> postorder({2, 1});
    Solution s = Solution();
    s.buildTree(inorder, postorder);
    // cout << s.buildTree(inorder, postorder)->val << " " << 1;
    return 0;
}
