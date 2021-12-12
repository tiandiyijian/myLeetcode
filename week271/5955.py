from typing import List
import IPython

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        def bin_search(arr, l, r, target):
            # print(arr, l, r, target)
            if target < arr[l][0]:
                return -1
            # IPython.embed()
            while l <= r:
                mid = l + (r-l) // 2
                # print(l, r, mid)
                if arr[mid][0] == target:
                    return mid
                elif arr[mid][0] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return r

        n = len(fruits)
        l, r = 0, n - 1
        idx = bin_search(fruits, l, r, startPos)
        print(idx)
        left_amount = []
        right_amount = []
        for i in range(idx, -1, -1):
            if fruits[i][0] + k < startPos:
                break
            left_amount.append([startPos-fruits[i][0], fruits[i][1] + (0 if not left_amount else left_amount[-1][1])])
        
        for i in range(idx+1, n):
            if fruits[i][0] - k > startPos:
                break
            right_amount.append([fruits[i][0]-startPos, fruits[i][1] + (0 if not right_amount else right_amount[-1][1])])
            # import IPython; IPython.embed()

        print('right_amount', right_amount)
        print('left_amount', left_amount)
        # print(left_amount, right_amount)
        n_right = len(right_amount)
        ans = 0
        right_idx = n_right-1
        if not left_amount and not right_amount:
            return 0
        if not left_amount:
            return right_amount[-1][1]
        if not right_amount:
            return left_amount[-1][1]
        for left in left_amount:
            current_step = left[0]
            if current_step <= k // 2:
                current_right_idx = bin_search(right_amount, 0, right_idx, k - 2*current_step)
                print(current_right_idx)
                if current_right_idx == -1:
                    break
                ans = max(left[1] + right_amount[current_right_idx][1], ans)
                print(current_step, right_amount[current_right_idx][0], ans)
                right_idx = current_right_idx
            else:
                break
        left_idx = len(left_amount) - 1
        for right in right_amount:
            current_step = right[0]
            if current_step < k // 2:
                current_left_idx = bin_search(left_amount, 0, left_idx, k - 2*current_step)
                if current_left_idx == -1:
                    break
                ans = max(ans, right[1]+left_amount[current_left_idx][1])
                left_idx = current_left_idx
            else:
                break
        ans = max(ans, left_amount[-1][1], right_amount[-1][1])
        return ans

fruits = [[0,96],[1,72],[4,80],[5,30],[6,40],[7,35],[8,9],[10,47],[11,47],[16,90],[17,14],[18,49],[19,71],[20,35],[21,98],[23,22],[24,84],[25,78],[26,29],[27,36],[28,84],[29,68],[30,60],[36,3],[37,14],[38,38],[40,80],[41,78],[44,12],[47,30],[49,8],[50,82],[52,78],[53,1],[54,9],[56,4],[57,92],[58,78],[59,75],[60,43],[61,100],[63,3],[64,64],[66,44],[67,61],[68,88],[69,14],[73,89],[75,21],[77,93],[78,91],[80,18],[84,7],[85,56],[86,100],[87,69],[88,89],[90,31],[92,66],[94,80],[96,94],[98,91],[99,33],[100,14]]
# 0
# 1

print(Solution().maxTotalFruits(fruits, 0, 1))
