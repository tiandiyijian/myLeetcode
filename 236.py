class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        return right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # containp = set()
        # containq = set()
        contain = []
        def dfs(root):
            if not root:
                return False, False
            a, b = dfs(root.left)
            c, d = dfs(root.right)
            # print(root.val, a, b, c, d)
            if root.val == p.val:
                if b or d:
                    contain.append(root)
                return True, b or d
            elif root.val == q.val:
                if a or c:
                    contain.append(root)
                return a or c, True
            else:
                if (a or c) and (b or d):
                    contain.append(root)
                return a or c, b or d
        dfs(root)
        # for c in contain:
        #     print(c.val)
        return contain[0]
        # 又是以前写得比现在好