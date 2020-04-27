from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length < 2:
            return nums

        def merge(start, middle, end):
            l, r = start, middle + 1
            tmp = nums[start:middle+1]
            i = start
            l = 0
            # print(start, middle, end)
            while l <= middle - start and r <= end:
                # print(tmp[l])
                # print(nums[r])
                if tmp[l] < nums[r]:
                    nums[i] = tmp[l]
                    l += 1
                else:
                    nums[i] = nums[r]
                    r += 1
                i += 1
            if r > end:
                nums[i:end+1] = tmp[l:]

        def sort(start, end):
            if start == end:
                return
            middle = (start + end) // 2
            sort(start, middle)
            sort(middle + 1, end)
            merge(start, middle, end)

        sort(0, length - 1)
        return nums

    def sortArray1(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length < 2:
            return nums

        def merge(start, middle, end):
            l, r = start, middle + 1
            tmp = nums[start:middle+1]
            i = start
            l = 0
            # print(start, middle, end)
            while l <= middle - start and r <= end:
                # print(tmp[l])
                # print(nums[r])
                if tmp[l] < nums[r]:
                    nums[i] = tmp[l]
                    l += 1
                else:
                    nums[i] = nums[r]
                    r += 1
                i += 1
            if r > end:
                nums[i:end+1] = tmp[l:]

        count = 1
        while count < length:
            i = 0
            while i + count < length:
                merge(i, i + count - 1, min(i + 2 * count - 1, length - 1))
                i += 2 * count
            print(f'count:{count}')
            print(nums)    
            count <<= 1
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.sortArray1([4, 2, 3, 1]))
