from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        size = m - k + 1
        ans = [0] * size

        q = deque(maxlen=k)

        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans[0] = nums[q[0]]
        idx = 1

        for i in range(k, m):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans[idx] = nums[q[0]]
            idx += 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print()
