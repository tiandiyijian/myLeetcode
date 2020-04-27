class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # res = [[None]] * n
        # for i in range(n):
        #     res[i] = [0] * n
        # i = 0
        # j = 0
        # pi = 0
        # pj = 0
        # dir = 0
        # count = 1
        # while res[i][j] == 0:
        #     res[i][j] = count
        #     count += 1
        #     if dir == 0:
        #         j = j + 1
        #     elif dir == 1:
        #         i = i + 1
        #     elif dir == 2:
        #         j = j - 1
        #     elif dir == 3:
        #         i = i - 1
        #     if i < 0 or i >= n or j < 0 or j >= n or res[i][j] != 0:
        #         if dir == 0:
        #             dir = 1
        #             i = i + 1
        #             j = j -1
        #         elif dir == 1:
        #             dir = 2
        #             i = i - 1
        #             j = j - 1
        #         elif dir == 2:
        #             dir = 3
        #             i = i - 1
        #             j = j + 1
        #         elif dir == 3:
        #             dir = 0
        #             i = i + 1
        #             j = j + 1
        # return res
        
        ans = [[0] * n for _ in range(n)]
        layer = n // 2 + n % 2
        num = 1
        for i in range(layer):
            ans[i][i : n - i] = list(range(num, num + n - 2*i))
            num += n - 2*i
            print(ans, num)
            for j in range(i + 1, n - i):
                ans[j][n - i - 1] = num
                num += 1
            print(ans, num)
            if n - 1 - i == i: break
            ans[n - 1 - i][n - i - 2 : i : -1] = list(range(num, num + n - 2*i - 2 ))
            num += n - 2*i - 2
            print(ans, num)
            if i == n - i - 1: break
            for j in range(n - i - 1, i, -1):
                ans[j][i] = num
                num += 1
            print(ans, num)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix(3))
