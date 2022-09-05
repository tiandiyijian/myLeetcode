from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        # 用一个三元组表示一棵树
        repeat = set()
        seen = dict()
        idx = 1

        def dfs(root):
            if not root:
                return 0
            tri = (root.val, dfs(root.left), dfs(root.right))

            if tri in seen:
                tree, curIdx = seen[tri]
                repeat.add(tree)
                return curIdx
            else:
                nonlocal idx
                seen[tri] = (root, idx)  # 只在第一次出现时才放进去，这样每次取出来的都是同一个，才可以正确去重
                idx += 1
                return idx - 1

        dfs(root)
        # print(repeat)
        # print(seen)
        return list(repeat)
