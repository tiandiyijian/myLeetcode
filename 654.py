# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        num = max(nums)
        idx = nums.index(num)
        return TreeNode(num, self.constructMaximumBinaryTree(nums[:idx]), self.constructMaximumBinaryTree(nums[idx+1:]))
