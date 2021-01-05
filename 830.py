class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        n = len(s)
        ans = []
        l = r = 0

        while l < n:
            r = l
            while r < n and s[r] == s[l]:
                r += 1
            if r - l >= 3:
                ans.append([l, r-1])
            l = r

        return ans


if __name__ == "__main__":
    s = Solution()
    print()
