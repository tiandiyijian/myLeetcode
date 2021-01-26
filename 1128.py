from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # 相当于统计每个元素出现了多少次
        # 可以自定义映射如(x, y)->10x+y
        # mp = collections.defaultdict(int)
        mp = [0] * 100
        ans = 0
        for a, b in dominoes:
            if a > b:
                a, b = b, a
            key = 10*a + b
            ans += mp[key]
            mp[key] += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
