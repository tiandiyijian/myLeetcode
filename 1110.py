from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)
        def helper(node, delete_parent, parent):
            if not node:
                return
            nonlocal ans
            if node.val in to_delete:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                left, right = node.left, node.right
                node.left = node.right = None
                helper(left, True, None)
                helper(right, True, None)
            else:
                if delete_parent:
                    ans.append(node)
                helper(node.left, False, node)
                helper(node.right, False, node)

        helper(root, True, None)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
