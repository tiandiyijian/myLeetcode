from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        def dfs(start, cur):
            ans.append(cur)
            if start == n:
                return
            for i in range(start, n):
                if (i > start and nums[i] == nums[i-1]):
                    continue
                # cur.append(nums[i])
                dfs(i+1, cur + [nums[i]])
                # cur.pop()

        dfs(0, [])
        return ans

    # def subsetsWithDupLoop(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     ans = [[]]
    #     n = len(nums)
    #     for _ in range(n):
    #         for i in range(n):
    #             if i > 0 and nums[i] == nums[i-1]:
    #                 continue
    #             ans =  ans + [s + [nums[i]] for s in ans]
    #     return ans

    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        def dfs(i, cur):
            if i == n:
                ans.append(cur)
                return
            if not cur or nums[i] != cur[-1]:
                dfs(i + 1, cur)
            dfs(i + 1, cur + [nums[i]])
        dfs(0, [])
        return ans

    def subsetsWithDup1Loop(self, nums):
        nums.sort()
        ans = [[]]
        n = len(nums)
        for i in range(n):
            tmp = []
            for s in ans:
                if not s or nums[i] != s[-1]:
                    tmp.append(s)
                tmp.append(s + [nums[i]])
            ans = tmp
        return ans

    def subsetsWithDup2(self, nums):
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        ans = [[]]
        for num, count in num_count.items():
            ans = [a + [num] * c for c in range(count + 1) for a in ans]
            # print(ans)
        return ans

    def subsetsWithDup3(self, nums: List[int]) -> List[List[int]]:
        adict = {}
        for i in nums:
            if i in adict:
                adict[i] += 1
            else:
                adict[i] = 1
        res = [[]]
        for i, v in adict.items():
            temp = res.copy()
            for j in res:
                temp.extend(j+[i]*(k+1) for k in range(v))
            res = temp
            print(res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup3([1, 2, 2]))
