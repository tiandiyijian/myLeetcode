from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        # 也可以用哈希表存下一个数组来查找
        sum_A = sum(A)
        sum_B = sum(B)
        change = False
        # if sum_A > sum_B:
        #     A, B = B, A
        #     sum_A, sum_B = sum_B, sum_A
        #     change = True
        diff = (sum_B - sum_A) // 2  # diff是负数也没关系
        B.sort()
        A.sort()
        j = 0
        for num in A:
            j = bisect.bisect_left(B, num + diff, j)
            if j != len(B) and B[j] == num + diff:
                # return [B[j], num] if change else [num, B[j]]
                return [num, B[j]]


if __name__ == "__main__":
    s = Solution()
    print()
