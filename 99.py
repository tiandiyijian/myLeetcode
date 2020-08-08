# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x = y = pred = None
        s = []
        while s or root:
            while root:
                s.append(root)
                root = root.left
            root = s.pop()
            if pred and root.val < pred.val:
                y = root
                if not x:
                    x = pred
                else:
                    break
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val

    def recoverTree2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        post = None
        pred = None
        def dfs(node: TreeNode):
            nonlocal pre, post, pred
            if not node:
                return
            dfs(node.left)
            # print(pred.val if pred else None, node.val)
            if pred and node.val < pred.val:
                post = node
                if not pre:
                    pre = pred
                else:
                    return
            pred = node
            dfs(node.right)

        dfs(root)
        pre.val, post.val = post.val, pre.val


if __name__ == "__main__":
    s = Solution()
    print()
