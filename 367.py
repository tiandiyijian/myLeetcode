class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low < high:
            mid = (low + high) // 2
            if (tmp := mid * mid) == num:
                return True
            elif tmp < num:
                low = mid + 1
            else:
                high = mid - 1
        return low * low == num