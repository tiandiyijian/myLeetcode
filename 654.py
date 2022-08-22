from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree1(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        num = max(nums)
        idx = nums.index(num)
        return TreeNode(num, self.constructMaximumBinaryTree(nums[:idx]), self.constructMaximumBinaryTree(nums[idx+1:]))

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 单调栈的解法是在是妙
        # 比前面的大就把前面的节点作为当前节点的左子树
        # 入栈的时候比前面的小就作为前面的节点的右子树
        if len(nums) == 0:
            return None

        s = []
        for n in nums:
            node = TreeNode(n)

            while s and s[-1].val < n:
                node.left = s.pop()
            
            if s:
                s[-1].right = node
            
            s.append(node)
        
        return s[0]     
