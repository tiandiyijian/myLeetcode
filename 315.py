from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * n
        indices = list(range(n))
        # print(indices)
        def merge(l, mid, r):
            # print('lmidr:', l, mid, r)
            # print('start', indices[l:r+1])
            tmp = indices[l:mid+1]
            start_1, start_2 = 0, mid + 1
            i = l
            # print(tmp, indices[start_2: r+1])
            while start_1 <= (mid - l) and start_2 <= r:
                if nums[tmp[start_1]] <= nums[indices[start_2]]:
                    indices[i] = tmp[start_1]
                    count[indices[i]] += start_2 - mid - 1
                    start_1 += 1
                else:
                    indices[i] = indices[start_2]
                    start_2 += 1
                i += 1
            # print('middle', indices)
            # print('ssi:', start_1, start_2, i)
            while start_1 <= (mid - l):
                indices[i] = tmp[start_1]
                count[indices[i]] += start_2 - mid - 1
                start_1 += 1
                i += 1
            # print('end', indices[l:r+1])
        def merge_sort(l, r):
            if l >= r:
                return
            mid = (l + r) // 2
            merge_sort(l, mid)
            merge_sort(mid + 1, r)
            merge(l, mid, r)

        merge_sort(0, n - 1)
        # print(indices)
        return count


if __name__ == "__main__":
    s = Solution()
    l = [1, 2, 0]
    print(s.countSmaller(l))