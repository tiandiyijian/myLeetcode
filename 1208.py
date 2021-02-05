from typing import List


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = r = cur_cost = 0
        n = len(s)
        while r < n:
            cur_cost += abs(ord(s[r]) - ord(t[r]))
            if cur_cost > maxCost:
                cur_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            r += 1
        return r - l


if __name__ == "__main__":
    s = Solution()
    print()
