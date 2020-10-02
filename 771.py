class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewel = set(J)
        ans = 0
        for s in S:
            if s in jewel:
                ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
