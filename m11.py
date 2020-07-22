from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if numbers[mid] > numbers[hi]:
                lo = mid + 1
            elif numbers[mid] < numbers[hi]:
                hi = mid
            else:
                hi -= 1
            print(lo, hi)
        return numbers[lo]

    def maxArray(self, numbers: List[int]) -> int:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            mid = (lo + hi) // 2 + 1
            # 因为mid要跟lo比较，所以mid不能等于lo，所以要加1
            if numbers[mid] > numbers[lo]:
                lo = mid
            elif numbers[mid] < numbers[lo]:
                hi = mid - 1
            else:
                lo += 1
            print(lo, hi)
        return numbers[lo]


if __name__ == "__main__":
    s = Solution()
    l = [5,6,6,1,2,3,4,5,5]
    print(s.maxArray(l))
