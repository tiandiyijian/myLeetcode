from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 实现 nums[(i + k) % n] = nums[i] 即可
        count = 0
        n = len(nums)
        k %= n

        for start in range(n):
            current = start
            pre_value = nums[start]
            while True:
                nxt = (current + k) % n
                pre_value, nums[nxt] = nums[nxt], pre_value
                count += 1
                current = nxt
                if count == n:
                    return
                if current == start:
                    break


if __name__ == "__main__":
    s = Solution()
    print()
