import sys
import time
class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        coins.sort(reverse=True)
        self.res = sys.maxsize
        def coinChange(index, amount, count):
            if amount == 0:
                self.res = min(self.res, count)
                return
            if index == len(coins):
                return
            numOfCoin = coins[index]
            for k in range(amount // numOfCoin, -1, -1):
                if k + count >= self.res:
                    break
                # if k + count < self.res:
                coinChange(index + 1, amount - k*numOfCoin, count + k)
            pass
        coinChange(0, amount, 0)
        return -1 if self.res == sys.maxsize else self.res

if __name__ == '__main__':
    solution = Solution()
    coins = [470,35,120,81,121]
    amount = 9825
    start = time.time()
    print(solution.coinChange(coins, amount))
    print(time.time() - start)