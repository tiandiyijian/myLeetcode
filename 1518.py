class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        num_full, num_empty = numBottles, 0
        while num_full > 0:
            ans += num_full
            tmp = num_full + num_empty
            num_full = tmp // numExchange
            num_empty = tmp % numExchange
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.numWaterBottles(15, 4))
