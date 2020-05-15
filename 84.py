from typing import List


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        length = len(heights)
        if length == 1:
            return heights[0]
        i = 0
        stack = []
        res = 0
        while i <= length:
            if len(stack) == 0 or (i < length and heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                height = heights[stack.pop()]
                print(i, height, stack)
                if stack:
                    rect = height * (i - stack[-1] - 1)
                else:
                    rect = height * i
                res = max(res, rect)
        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # if not heights:
        #     return 0
        # ans = 0
        # for i in range(len(heights)):
        #     h = heights[i]
        #     l = 1
        #     for j in range(i + 1, len(heights)):
        #         if heights[j] >= h:
        #             l += 1
        #         else:
        #             break
        #     for j in range(i - 1, -1, -1):
        #         if heights[j] >= h:
        #             l += 1
        #         else:
        #             break
        #     ans = max(ans, l * h)
        # return ans
        stack = [-1]
        heights.append(0)
        ans = 0
        for i in range(0, len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                right = i - 1
                height = heights[stack.pop()]
                left = stack[-1] + 1
                # print(left, right)
                ans = max(ans, height * (right - left + 1))
            stack.append(i)
            # print(stack)
        return ans


if __name__ == "__main__":
    s = Solution()
    hs = [2, 1, 5, 6, 2, 3]
    hs = [2, 1, 2]
    print(s.largestRectangleArea(hs))
    # 又是以前做过的又忘了