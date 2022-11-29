class Solution:
    def minOperations(self, s: str) -> int:
        return min(
            sum(c == '0' if i & 1 else c == '1' for i, c in enumerate(s)),
            sum(c == '1' if i & 1 else c == '0' for i, c in enumerate(s)),
        )
