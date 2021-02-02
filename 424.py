from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        l = r = 0
        count = [0] * 26
        maxn = 0
        while r < n:
            count[ord(s[r]) - ord('A')] += 1
            maxn = max(maxn, count[ord(s[r]) - ord('A')])
            # while r - l + 1 - maxn > k:
            # 这里不需要使用while，这种条件下虽然窗口可能不符合条件，但是它对正确答案没有影响
            # 即窗口虽然没有变小使得它符合条件，但是它也没有变大而对答案产生影响
            if r - l + 1 - maxn > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
            # ans = max(ans, r - l)
        # return ans
        return r - l


if __name__ == "__main__":
    s = Solution()
    print()
