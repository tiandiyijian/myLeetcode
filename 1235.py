from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        n = len(startTime)
        indices = sorted(range(n), key=lambda x: startTime[x])
        max_start = startTime[indices[-1]]

        dp = [0] * n
        for i in range(n - 1, -1, -1):
            idx = indices[i]
            if i == n - 1:
                # 最后一个只能选自己
                dp[i] = profit[idx]
                continue
            if endTime[idx] > max_start:
                # 结束时间超过最大开始时间
                # 如果选的话就只能选自己
                dp[i] = max(dp[i + 1], profit[idx])
                continue

            # 找到第一个开始时间大于等于当前结束时间的job
            end = endTime[idx]
            left, right = i, n - 1
            while left < right:
                mid = (left + right) >> 1
                time = startTime[indices[mid]]
                if end <= time:
                    right = mid
                else:
                    left = mid + 1
            dp[i] = max(dp[i + 1], profit[idx] + dp[left])

        return dp[0]
