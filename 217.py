class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            else: s.add(num)
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        # return any((c > 1 for c in Counter(nums).values()))
        return len(nums) > len(set(nums))


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,2,3]))