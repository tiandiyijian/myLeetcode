from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False

        avg = 0
        for i in range(n):
            nums[i] *= n
            avg += nums[i]

        avg /= n
        # 让平均值为0
        for i in range(n):
            nums[i] -= avg

        A, B = nums[: n // 2], nums[n // 2 :]
        length = len(A)
        A_set = set()
        for s in range(1, 2**length):
            cur_sum = 0
            for i in range(length):
                if s & (1 << i):
                    cur_sum += A[i]
            if cur_sum == 0:
                return True
            A_set.add(cur_sum)

        length = len(B)
        max_s = 2**length
        for s in range(1, max_s):
            cur_sum = 0
            for i in range(length):
                if s & (1 << i):
                    cur_sum += B[i]
            if cur_sum == 0:
                return True
            if s != (max_s - 1) and -cur_sum in A_set:
                return True

        return False


print(
    Solution().splitArraySameAverage(
        [
            3863,
            703,
            1799,
            327,
            3682,
            4330,
            3388,
            6187,
            5330,
            6572,
            938,
            6842,
            678,
            9837,
            8256,
            6886,
            2204,
            5262,
            6643,
            829,
            745,
            8755,
            3549,
            6627,
            1633,
            4290,
            7,
        ]
    )
)
