from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # 首先根据总1的个数确定每个部分1的个数
        # 然后最右边那部分的值就可以确定了(前导0不影响值的大小)
        # 再根据这个值去判断左边和中间的部分
        n = len(arr)
        tot = sum(arr)
        cnt, mod = divmod(tot, 3)
        if mod != 0:
            return [-1, -1]
        if cnt == 0:
            return [0, 2]

        right = 0
        cur_cnt = 0
        right_first_one = n
        for i in range(n - 1, -1, -1):
            if arr[i] == 1:
                if right_first_one == n:
                    right_first_one = i
                cur_cnt += 1
                if cur_cnt == cnt:
                    break
        right = i

        for i in range(n):
            if arr[i] == 1:
                left_first_one = i
                break

        for i in range(n - right):
            if arr[left_first_one + i] != arr[right + i]:
                return [-1, -1]

        mid = left_first_one + n - right

        for i in range(mid, n):
            if arr[i] == 1:
                mid_first_one = i
                break

        if mid_first_one + n - right > right:
            return [-1, -1]

        for i in range(n - right):
            if arr[mid_first_one + i] != arr[right + i]:
                return [-1, -1]

        return [mid - 1, mid_first_one + n - right]
