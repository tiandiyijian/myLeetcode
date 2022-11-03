class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        for k in range(1, len(sequence) // len(word) + 1):
            if word * k in sequence:
                ans = k
            else:
                break

        return ans
