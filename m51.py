from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        self.pairs = 0
        def merge(nums, s1, s2, size1, size2):
            tmp = nums[s1:s1+size]
            i0 = s1
            i1, i2 = 0, s2
            end2 = s2 + size2
            print(s1, s2, size1, size2)
            while i1 < size1 and i2 < end2:
                if tmp[i1] <= nums[i2]:
                    nums[i0] = tmp[i1]
                    i1 += 1
                else:
                    nums[i0] = nums[i2]
                    i2 += 1
                    self.pairs += size1 - i1
                i0 += 1
            while i1 < size1:
                nums[i0] = tmp[i1]
                i1 += 1
                i0 += 1
            # while i2 < end2:
        size = 1
        while size < length:
            for i in range(0, length-size, size*2): # i + size < length
                merge(nums, i, i + size, size, min(length-i-size, size))
            size *= 2
        print(nums)
        return self.pairs


if __name__ == "__main__":
    s = Solution()
    l = [7,5,6,4,1]
    print(s.reversePairs(l))