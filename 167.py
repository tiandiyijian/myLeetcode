from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 二分查找
        for i in range(len(numbers) - 1):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            if numbers[r] < tmp or numbers[l] > tmp:
                continue
            while l <= r:
                mid = (l + r) // 2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] > tmp:
                    r = mid - 1
                else:
                    l = mid + 1

    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        # 双指针
        l, r = 0, len(numbers) - 1
        while l < r:
            tmp = numbers[l] + numbers[r]
            if tmp == target:
                return [l+1, r+1]
            elif tmp < target:
                l += 1
            else:
                r -= 1

if __name__ == "__main__":
    s = Solution()
    nums = [2,7,11,15]
    t = 9
    print(s.twoSum1(nums, t))