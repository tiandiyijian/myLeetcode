from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        candys = [1] * size

        for i in range(1, size):
            if ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1] + 1

        total = candys[-1]
        for i in range(size - 2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candys[i] = max(candys[i], candys[i+1] + 1)
            total += candys[i]

        # print(candys)
        # return sum(candys)
        return total


if __name__ == "__main__":
    s = Solution()
    print()
