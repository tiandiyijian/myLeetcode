# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()
        i, j = 0, length - 1
        while i < j:
            mid = (i + j) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                i = mid + 1
            else:
                j = mid
        # print(i)
        maxIdx = i
        i, j = 0, maxIdx
        while i <= j:
            mid = (i + j) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num < target:
                i = mid + 1
            else:
                j = mid - 1
        i, j = maxIdx, length - 1
        while i <= j:
            mid = (i + j) // 2
            num = mountain_arr.get(mid)
            if num == target:
                return mid
            elif num > target:
                i = mid + 1
            else:
                j = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print()
