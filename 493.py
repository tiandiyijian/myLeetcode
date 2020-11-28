from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def count(left, right):
            if left >= right:
                return 0
            mid = (left + right) >> 1

            n1 = count(left, mid)
            n2 = count(mid + 1, right)

            ans = n1 + n2
            # l = r = mid + 1
            l = left
            r = mid + 1

            while l <= mid:
                while r <= right and nums[l] > nums[r] * 2:
                    r += 1
                ans += r - mid - 1
                l += 1

            local_sorted_num = nums[left:mid+1]
            p, q = 0, mid + 1
            for i in range(left, right + 1):
                if p >= len(local_sorted_num):
                    nums[i] = nums[q]
                    q += 1
                elif q > right:
                    nums[i] = local_sorted_num[p]
                    p += 1
                else:
                    if local_sorted_num[p] <= nums[q]:
                        nums[i] = local_sorted_num[p]
                        p += 1
                    else:
                        nums[i] = nums[q]
                        q += 1
            return ans

        ans = count(0, len(nums) - 1)
        # print(nums)
        return ans

if __name__ == "__main__":
    s = Solution()
    l = [2147483647,2147483647,-2147483647,-2147483647,-2147483647,2147483647]
    print(s.reversePairs(l))