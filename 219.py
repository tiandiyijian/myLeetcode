class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        map = {}
        for i, num in enumerate(nums):
            if num in map and i - map[num] <= k:
                return True
            else: map[num] = i
        return False



if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,3,1], 3))