import bisect


class Solution:

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 错误解法，因为不能保证把当前窗口中的答案都改变为当前窗口中最左边的答案就可以得到最大连续相同子串
        # n = len(answerKey)
        # ans = 0
        # l = 0
        # while True:
        #     r = l
        #     while r < n and answerKey[r] == answerKey[l]:
        #         r += 1
        #     firstR = r
        #     change = 0
        #     while r < n and change < k:
        #         if answerKey[r] != answerKey[l]:
        #             change += 1
        #         r += 1
        #     while r < n and answerKey[r] == answerKey[l]:
        #         r += 1
        #     ans = max(ans, r - l)
        #     print(l, r)
        #     if r >= n:
        #         break
        #     l += 1
        # return ans

        # 属于是把题目中的相关标签二分查找、前缀和、滑动窗口都用上了
        # 其实分别对T和F做一次滑动窗口就行了
        # 但对前缀和做二分查找确实能加快滑动的速度
        n = len(answerKey)
        t_prefix = [0] * (n + 1)
        f_prefix = [0] * (n + 1)
        for i in range(n):
            t_prefix[i + 1] = t_prefix[i]
            f_prefix[i + 1] = f_prefix[i]
            if answerKey[i] == 'T':
                t_prefix[i + 1] += 1
            else:
                f_prefix[i + 1] += 1

        ans = 0
        l = r = 0
        while l <= n:
            r = bisect.bisect_right(t_prefix, t_prefix[l] + k, lo=r)
            ans = max(ans, r - l - 1)
            l += 1

        l = r = 0
        while l <= n:
            r = bisect.bisect_right(f_prefix, f_prefix[l] + k, lo=r)
            ans = max(ans, r - l - 1)
            l += 1

        return ans


l = "FFFTTFTTFT"
k = 3
print(Solution().maxConsecutiveAnswers(l, k))
