from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = nums[:k]
        window.sort()
        odd = True if k & 1 else False
        mid = k >> 1
        ans = [window[mid] if odd else (window[mid] + window[mid-1])/2]

        for i in range(k, len(nums)):
            if nums[i] == nums[i - k]:
                ans.append(ans[-1])
            else:
                # print(window, nums[i-k])
                window.pop(bisect.bisect_left(window, nums[i - k]))
                bisect.insort(window, nums[i])
                ans.append(window[mid] if odd else (
                    window[mid] + window[mid-1])/2)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
