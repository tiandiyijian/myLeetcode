from typing import List
from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 0
        # positions = deque([0])
        # jumps = 0
        # while True:
        #     length = len(positions)
        #     maxPos = positions[0]
        #     print(maxPos)
        #     for _ in range(length):
        #         pos = positions.pop()
        #         if pos + nums[pos] >= len(nums) - 1:
        #             return jumps + 1
        #         if pos + nums[pos] > maxPos:
        #             positions.extendleft(range(maxPos + 1, pos + nums[pos] + 1))
        #     jumps += 1
        l = r = 0
        jumps = 0
        while True:
            if r >= len(nums) - 1:
                return jumps
            nl = r + 1
            for i in range(l, r + 1):
                r = max(i + nums[i], r)
            jumps += 1
            # if r >= len(nums) - 1:
            #     return jumps
            l = nl

if __name__ == "__main__":
    s = Solution()
    l = [2, 3, 1, 1, 4]
    l = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
    print(s.jump(l))
