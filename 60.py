import operator
from functools import reduce


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'        
        nums = [str(i) for i in range(1, n + 1)]
        pre = []
        k -= 1
        count = reduce(operator.mul, range(1, n))
        n -= 1
        while k > 0:
            idx = k // count
            k = k % count
            pre.append(nums.pop(idx))
            count //= n
            n -= 1
            # print(pre, k, nums)
        return ''.join(pre) + ''.join(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.getPermutation(4, 9))
