from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 也可以用滑动窗口，滑要的或者不要的最后减去都行
        # 记录前缀和和后缀和确实没用
        # left_sum = [0] + cardPoints[:k]
        # right_sum = [0] + cardPoints[-1:-1-k:-1]
        # for i in range(1, k+1):
        #     left_sum[i] += left_sum[i-1]
        #     right_sum[i] += right_sum[i-1]
        # ans = 0
        # for i in range(k+1):
        #     ans = max(left_sum[i] + right_sum[k-i], ans)
        # return ans
        left_sum = sum(cardPoints[:k])
        right_sum = 0
        max_sum = left_sum
        for i in range(k):
            left_sum -= cardPoints[k - 1 - i]
            right_sum += cardPoints[-i - 1]
            max_sum = max(max_sum, left_sum + right_sum)
        return max_sum


if __name__ == "__main__":
    s = Solution()
    print()
