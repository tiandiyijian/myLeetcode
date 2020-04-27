from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        self.ans = []
        self.nums = nums
        self.tmp = []
        self.length = len(nums)
        def choose_num():
            if len(self.tmp) == self.length:
                self.ans.append(self.tmp.copy())
                return
            for i in range(len(self.nums)):
                tmp_num = self.nums.pop(i)
                self.tmp.append(tmp_num)
                choose_num()
                self.tmp.pop()
                self.nums.insert(i, tmp_num)
        choose_num()
        return self.ans

    def permute1(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        self.ans = []
        self.nums = nums
        # self.tmp = []
        self.length = len(nums)
        def choose_num(pos):
            if pos == self.length-1:
                self.ans.append(self.nums[:])
                return
            for i in range(pos, len(self.nums)):
                self.nums[pos], self.nums[i] = self.nums[i], self.nums[pos]
                choose_num(pos + 1)
                self.nums[pos], self.nums[i] = self.nums[i], self.nums[pos]
        choose_num(0)
        return self.ans
        
    def permute2(self, nums: List[int]) -> List[List[int]]:
        if not nums: return nums
        self.ans = []
        def choose_num(nums, permutation):
            if not nums:
                self.ans.append(permutation)
                return
            for i in range(len(nums)):
                choose_num(nums[:i] + nums[i + 1:], permutation + [nums[i]])
        choose_num(nums, [])
        return self.ans


if __name__ == "__main__":
   s = Solution()
   print(s.permute2([1,2,3]))