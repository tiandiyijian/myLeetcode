from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        if shorter == longer:
            return [k * shorter]
        # ans = [0] * (k + 1)
        d = longer - shorter
        start = shorter * k
        # for i in range(k+1):
        #     # ans[i] = (i * longer + (k - i) * shorter)
        #     ans[i] = shorter * k + i * d
        ans = [start + i * d for i in range(k + 1)]
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.divingBoard(1, 2, 3))
