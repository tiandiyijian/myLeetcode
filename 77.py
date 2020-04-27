class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        ans = []
        set = []
        def helper(start, set, k):
            if len(set) == k:
                ans.append(set)
            else:
                for j in range(start, len(nums)):
                    helper(j+1, set + [nums[j]], k)
                

        if k > n or n < 1:
            return ans
        nums = list(range(1, n+1))
        helper(0, [], k)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.combine(3, 2))






