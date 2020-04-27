from typing import List
import collections

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # length = len(nums)
        # if length < 2:
        #     return True
        # position = collections.deque()
        # position.appendleft(0)
        # while position:
        #     pos = position.pop()
        #     if pos >= length - 1:
        #         return True
        #     if nums[pos] > 0:
        #         position.extendleft(list(range(pos+1, pos+nums[pos]+1)))
        # return False
        zeroCount = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= zeroCount:
                zeroCount += 1
            else:
                zeroCount = 0
        return zeroCount == 0

if __name__ == "__main__":
    s = Solution()
    l = [2,3,1,1,4]
    l = [3,2,1,0,4]
    print(s.canJump(l))