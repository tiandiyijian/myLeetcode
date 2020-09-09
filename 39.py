from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def helper(seq, seq_sum, idx):
            if seq_sum == target:
                ans.append(seq)
            elif seq_sum > target or idx >= len(candidates):
                return
            for i in range(idx, len(candidates)):
                helper(seq + [candidates[i]], seq_sum + candidates[i], i)
        
        helper([], 0, 0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,5], 8))
