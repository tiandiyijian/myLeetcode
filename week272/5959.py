from typing import List
import bisect


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def LIS(arr: List[int]) -> int:
            # print(arr)
            choose = [arr[0]]
            # choose_1 = [arr[0]]
            for i in range(1, len(arr)):
                if arr[i] >= choose[-1]:
                    choose.append(arr[i])
                else:
                    idx = bisect.bisect_right(choose, arr[i])
                    choose[idx] = arr[i]

                # if arr[i] >= choose_1[-1]:
                #     choose_1.append(arr[i])
                # else:
                #     idx1 = bisect.bisect_left(choose_1, arr[i])
                #     choose_1[idx1] = arr[i]
                # print(choose)
                # print(choose_1, '\n')
            return len(choose)

        ans = 0
        n = len(arr)
        for i in range(k):
            j = 0
            tmp_arr = []
            while (idx := i + j * k) < n:
                tmp_arr.append(arr[idx])
                j += 1
            ans += len(tmp_arr) - LIS(tmp_arr)
        return ans


arr = [2, 2, 2, 2, 2, 1, 1, 4, 4, 3, 3, 3, 3, 3]
k = 1
print(Solution().kIncreasing(arr, k))
