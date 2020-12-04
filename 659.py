from collections import Counter
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count_map = Counter(nums)
        end_map = Counter()
        for num in nums:
            if count := count_map.get(num, 0):
                if prev_end := end_map.get(num - 1, 0):
                    end_map[num-1] = prev_end + 1
                    end_map[num] += 1
                    count_map[num] = count - 1
                else:
                    if count_map[num+1] and count_map[num+2]:
                        end_map[num+2] += 1
                        count_map[num] -= 1
                        count_map[num+1] -= 1
                        count_map[num+2] -= 1
                    else:
                        return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPossible([1, 2, 3, 3, 4, 5]))
