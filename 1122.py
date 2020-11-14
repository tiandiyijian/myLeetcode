from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = [0] * 1001
        for num in arr1:
            freq[num] += 1
        ans = []

        for num in arr2:
            if freq[num] > 0:
                ans += [num] * freq[num]
                freq[num] = 0
        for i in range(1001):
            if freq[i] > 0:
                ans += [i] * freq[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
