from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        num_sum = [0] + nums
        for i in range(1, len(num_sum)):
            num_sum[i] += num_sum[i-1]

        def count(left, right):
            if left == right:
                return 0
            mid = (left + right) >> 1

            n1 = count(left, mid)
            n2 = count(mid + 1, right)

            ans = n1 + n2
            l = r = mid + 1
            for i in range(left, mid + 1):
                pre_sum = num_sum[i]
                if num_sum[l] - pre_sum > upper:
                    continue
                while l <= right and num_sum[l] - pre_sum < lower:
                    l += 1
                if l > right:
                    break
                while r <= right and num_sum[r] - pre_sum <= upper:
                    r += 1
                # r -= 1
                # print(r, l)
                ans += r - l
                # while l <= right and num_sum[l] - num_sum[i] < lower: l += 1
                # while r <= right and num_sum[r] - num_sum[i] <= upper: r += 1
                # ans += r - l

            local_sorted_sum = num_sum[left:mid+1]
            p, q = 0, mid + 1
            for i in range(left, right + 1):
                if p >= len(local_sorted_sum):
                    num_sum[i] = num_sum[q]
                    q += 1
                elif q > right:
                    num_sum[i] = local_sorted_sum[p]
                    p += 1
                else:
                    if local_sorted_sum[p] <= num_sum[q]:
                        num_sum[i] = local_sorted_sum[p]
                        p += 1
                    else:
                        num_sum[i] = num_sum[q]
                        q += 1
            # print(left, right, ans)
            return ans

        ans = count(0, len(num_sum) - 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    nums =  [-2,5,-1]
    lower = -2
    upper = 2
    print(s.countRangeSum(nums, lower, upper))
