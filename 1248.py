from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # length = len(nums)
        # if length < k:
        #     return 0
        # for i in range(length):
        #     nums[i] = 0 if nums[i] % 2 == 0 else 1
        # count = 0
        # for i in range(length - k + 1):
        #     tmpSum = 0
        #     for j in range(i, length):
        #         tmpSum += nums[j]
        #         if tmpSum == k:
        #             count += 1
        #         elif tmpSum > k:
        #             break
        # return count

        length = len(nums)
        indices = []
        if length < k:
            return 0
        for i in range(length):
            if nums[i] % 2 == 1:
                indices.append(i)
        if len(indices) < k:
            return 0
        count = 0
        for i in range(len(indices) - k + 1):
            left, right = indices[i], indices[i + k - 1]
            if i == 0:
                small = left
            else:
                small = left - indices[i-1] - 1
            if i == len(indices) - k:
                large = length - right - 1
            else:
                large = indices[i+k] - right - 1
            count += 1 + small + large + small * large
        return count


if __name__ == "__main__":
    s = Solution()
    l = [1, 1, 2, 1, 1]
    l = [1, 2, 1, 2, 2, 1, 2]
    print(s.numberOfSubarrays(l, 2))
