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
                print(i,height,stack)
                if stack:
                    rect = height * (i - stack[-1] - 1)
                else:
                    rect = height * i
                res = max(res, rect)
        return res
