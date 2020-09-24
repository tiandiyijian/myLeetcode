from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        base = None
        count = 0
        max_count = 0
        def helper(root):
            nonlocal base, count, max_count, ans
            if base is not None and root.val == base:
                count += 1
                if count > max_count:
                    max_count = count
                    ans = [base]
                elif count == max_count:
                    ans.append(base)
            else:
                base = root.val
                count = 1
                if count > max_count:
                    max_count = count
                    ans = [base]
                elif count == max_count:
                    ans.append(base)
             
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right is not root:
                    pre = pre.right
                if pre.right is root:
                    helper(root)
                    pre.right = None
                    root = root.right
                else:
                    pre.right = root
                    root = root.left
            else:
                helper(root)
                root = root.right
        return ans


if __name__ == "__main__":
    s = Solution()
    print()