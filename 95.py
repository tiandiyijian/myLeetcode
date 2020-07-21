from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def buildTree(root, left_list, right_list):
            ans = []
            # print(root, left_list, right_list)
            left = []
            for i in range(len(left_list)):
                left.extend(
                    buildTree(left_list[i], left_list[:i], left_list[i+1:]))
            right = []
            for j in range(len(right_list)):
                right.extend(buildTree(
                    right_list[j], right_list[:j], right_list[j+1:]))
            if not left:
                left = [None]
            if not right:
                right = [None]
            for l in left:
                for r in right:
                    tmp = TreeNode(root)
                    tmp.left = l
                    tmp.right = r
                    ans.append(tmp)
            return ans
        ans = []
        for i in range(1, n + 1):
            ans.extend(buildTree(i, list(range(1, i)), list(range(i+1, n+1))))
        return ans
        # 思路正确，代码还可以写简单点，看下次碰见能写成什么样吧


if __name__ == "__main__":
    s = Solution()
    print(s.generateTrees(3))
