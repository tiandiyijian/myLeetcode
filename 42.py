from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0
        idx = maxHeight = 0
        for i in range(length):
            if height[i] > maxHeight:
                idx, maxHeight = i, height[i]
        ans = 0
        tmpMax = 0
        # print(idx, maxHeight)
        for i in range(idx):
            if height[i] > tmpMax:
                tmpMax = height[i]
            else:
                ans += tmpMax - height[i]
                # print(i)
        tmpMax = 0
        for i in range(length-1, idx, -1):
            if height[i] > tmpMax:
                tmpMax = height[i]
            else:
                ans += tmpMax - height[i]
                # print(i)
        return ans


if __name__ == "__main__":
    s = Solution()
    l = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    l = [1, 0, 2]
    print(s.trap(l))
