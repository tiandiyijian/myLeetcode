from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num
        indexFromRight = 0
        # print(res)
        while res & 1 == 0:
            res >>= 1
            indexFromRight += 1
        a, b = 0, 0
        # print(indexFromRight)
        for num in nums:
            if (num >> indexFromRight) & 1 == 1:
                a ^= num
            else:
                b ^= num
        return [a, b] 

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumbers([4,1,4,6]))