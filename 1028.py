# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.idx = 0

        def dfs(depth):
            for i in range(self.idx, self.idx+depth):
                if S[i] != '-':
                    return None
            self.idx += depth
            next_idx = S.find('-', self.idx)
            if next_idx == -1:
                return TreeNode(int(S[self.idx:]))
            # print(S[self.idx:next_idx])
            # print(self.idx, S[self.idx], next_idx, S[next_idx], f'depth={depth}')
            root = TreeNode(int(S[self.idx: next_idx]))
            self.idx = next_idx

            for i in range(next_idx, next_idx+depth+1):
                if S[i] != '-':
                    return root

            root.left = dfs(depth+1)
            root.right = dfs(depth+1)
            return root
        return dfs(0)


if __name__ == "__main__":
    s = Solution()
    S = "1-2--3---4-5--6---7"
    print(s.recoverFromPreorder(S))
