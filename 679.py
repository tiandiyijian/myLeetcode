from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                tmp = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        tmp.append(nums[k])
                a, b = nums[i], nums[j]
                tmp.append(a + b)
                if self.judgePoint24(tmp):
                    return True
                tmp.pop()
                tmp.append(a * b)
                if self.judgePoint24(tmp):
                    return True
                tmp.pop()
                if abs(b) > 1e-6:
                    tmp.append(a / b)
                    if self.judgePoint24(tmp):
                        return True
                    tmp.pop()
                if abs(a) > 1e-6:
                    tmp.append(b / a)
                    if self.judgePoint24(tmp):
                        return True
                    tmp.pop()
                tmp.append(a - b)
                if self.judgePoint24(tmp):
                    return True
                tmp.pop()
                tmp.append(b - a)
                if self.judgePoint24(tmp):
                    return True
                tmp.pop()
        return False


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 1, 2]
    print(s.judgePoint24(nums))
