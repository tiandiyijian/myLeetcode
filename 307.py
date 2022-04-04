from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.size = int(n**0.5)
        self.sums = [0] * (n // self.size + 1)
        self.nums = nums
        for i in range(n):
            self.sums[i // self.size] += nums[i]
        # print(self.nums, self.sums, self.size)

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        l, r = left // self.size, right // self.size
        if l == r:
            return sum(self.nums[left:right + 1])
        return sum(self.nums[left:(l + 1) * self.size]) + sum(
            self.sums[l + 1:r]) + sum(self.nums[r * self.size:right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)