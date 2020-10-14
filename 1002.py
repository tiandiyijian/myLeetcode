import collections
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        counter = collections.Counter(A[0])
        for i in range(1, len(A)):
            tmp_counter = collections.Counter(A[i])
            for key in counter:
                if key in tmp_counter:
                    counter[key] = min(counter[key], tmp_counter[key])
                else:
                    counter[key] = 0
        for key, val in counter.items():
            ans.extend([key] * val)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
