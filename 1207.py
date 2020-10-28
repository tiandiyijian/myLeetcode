from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        dummy = [1] * (len(arr) + 1)
        for val in count.values():
            if dummy[val] == 0:
                return False
            dummy[val] = 0
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
