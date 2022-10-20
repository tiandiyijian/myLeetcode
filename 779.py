class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 01
        # 0110
        # 01101001
        # 0110100110010110
        # 前半段和上一行一样，后半段翻转

        def dfs(n, k, flip):
            # print(n, k, flip)
            if n == 1:
                return 1 if flip else 0

            mid = 2 ** (n - 2)
            if k > mid:
                return dfs(n - 1, k - mid, not flip)
            else:
                return dfs(n - 1, k, flip)

        return dfs(n, k, False)
