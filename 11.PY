class Solution:
    def maxArea(self, height: list) -> int:
        length = len(height)
        i = 0
        j = length - 1
        maxArea = 0
        while i < j:
            # print(f'{i} {j}')
            maxArea = max(maxArea, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                tmp = height[i]
                while height[i] <= tmp:
                    i += 1
            else:
                tmp = height[j]
                while height[j] <= tmp and i < j:
                    j -= 1
        return maxArea

if __name__ == "__main__":
    S = Solution()
    print(S.maxArea([1,8,6,2,5,4,8,3,7]))