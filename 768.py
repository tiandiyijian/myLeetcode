from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # 只要当前遍历到的最大值(要考虑重复)和排序后的数组能够对上就可以分一个块
        n = len(arr)
        arr1 = sorted(arr)
        ans = 0

        curMax = -1
        curMaxCnt = 0
        for i in range(n):
            if arr[i] > curMax:
                curMax = arr[i]
                curMaxCnt = 1
            elif arr[i] == curMax:
                curMaxCnt += 1

            if curMax == arr1[i]:
                if curMaxCnt > 1:
                    curMaxCnt -= 1
                else:
                    ans += 1
                    curMaxCnt = 0
                    curMax = -1

        return ans

    def maxChunksToSorted1(self, arr: List[int]) -> int:
        # 单调栈有点妙
        # 如果当前遍历到的元素小于当前块最大值那就要和前面的块的最大值比较
        #   如果比它还要小的话就要和前面的块融合
        # 如果大于等于当前块的最大值那就可以自成一个块
        stack = []
        for a in arr:
            if len(stack) == 0 or a >= stack[-1]:
                stack.append(a)
            else:
                mx = stack.pop()
                while stack and stack[-1] > a:
                    stack.pop()
                stack.append(mx)
        return len(stack)


arr = [2, 1, 5, 2, 3, 4, 7, 8]
print(Solution().maxChunksToSorted1(arr))
