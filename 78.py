class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res = res + [[num] + set for set in res]
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
