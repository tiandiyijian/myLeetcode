from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(l, r):
            if l > r:
                return None
            mid = (l + r) // 2
            print(mid)
            root = TreeNode(nums[mid])
            left = helper(l, mid - 1)
            right = helper(mid + 1, r)
            root.left, root.right = left, right
            return root
        return helper(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.sortedArrayToBST([-10,-3,0,5,9]))