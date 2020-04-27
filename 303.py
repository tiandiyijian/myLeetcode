class NumArray:

    def __init__(self, nums: List[int]):
        temSum = 0
        self.sums = []
        for i in nums:
            temSum += i
            self.sums.append(temSum)

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.sums[j]
        return self.sums[j] - self.sums[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)