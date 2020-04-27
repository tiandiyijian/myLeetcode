import sys

class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        distance = sys.maxsize
        ans = 0
        for i in range(len(nums)-2):
            # if nums[i] > target and target > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                tmpDistance = abs(target - sum)
                if tmpDistance < distance:
                    ans = sum
                    distance = tmpDistance
                if sum > target: k -= 1
                elif sum < target: j += 1
                else: return ans
        return ans

if __name__ == "__main__":
    S = Solution()
    print(S.threeSumClosest([-1,2,1,-4], 1))