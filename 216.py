from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(seq, remain, num):
            if len(seq) == k and remain == 0:
                ans.append(seq)
                return
            elif len(seq) > k or num > 9:
                return
            if num <= remain:
                helper(seq + [num], remain - num, num + 1)
                helper(seq, remain, num + 1)
        
        helper([], n, 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3,7))