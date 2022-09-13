class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)

        for i in range(n):
            maxNum = max(nums[i:])
            if nums[i] == maxNum:
                continue
            for j in range(n - 1, i, -1):
                if nums[j] == maxNum:
                    nums[i], nums[j] = nums[j], nums[i]
                    return int("".join(nums))

        return num
