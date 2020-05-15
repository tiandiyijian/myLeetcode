from typing import List
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        size = len(nums)
        sumArray = [0] * (size + 1)
        count = 0
        sumDict = collections.defaultdict(int, {0:1})
        for i in range(0, size):
            sumArray[i+1] = nums[i] + sumArray[i]
            count += sumDict.get(sumArray[i+1] - k, 0)
            sumDict[sumArray[i+1]] += 1
        # print(sumArray, sumDict)
        return count

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    print(s.subarraySum([1], 0))
