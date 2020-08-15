from typing import List
import collections


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        ans = 0
        record = collections.defaultdict(int, {0: 1})
        sumArray = [0] * (len(A) + 1)
        for i in range(len(A)):
            sumArray[i+1] = (A[i] + sumArray[i]) % K
            ans += record[sumArray[i+1]]
            record[sumArray[i+1]] += 1
        return ans
    
    def subarraysDivByK2(self, A: List[int], K: int) -> int:
        remainder_count = collections.defaultdict(int)
        remainder_count[0] = 1
        current_remainder = 0
        ans = 0
        for i in range(len(A)):
            current_remainder = (current_remainder + A[i]) % K
            ans += remainder_count[current_remainder]
            remainder_count[current_remainder] += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.subarraysDivByK2([4, 5, 0, -2, -3, 1], 5))
