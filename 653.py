from tkinter.tix import Tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # 这个写法太妙了，很好地利用了Python的生成器，不用自己构造栈模拟左右指针的移动
        def inorder(root: TreeNode):
            if not root:
                return
            yield from inorder(root.left)
            yield root.val
            yield from inorder(root.right)

        def inorder_reverse(root: TreeNode):
            if not root:
                return
            yield from inorder_reverse(root.right)
            yield root.val
            yield from inorder_reverse(root.left)

        left_gen, right_gen = inorder(root), inorder_reverse(root)
        left, right = next(left_gen), next(right_gen)
        while left < right:
            print(left, right)
            if (tmp := left + right) == k:
                return True
            elif tmp > k:
                right = next(right_gen)
            else:
                left = next(left_gen)
        return False


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().findTarget(root, 3))