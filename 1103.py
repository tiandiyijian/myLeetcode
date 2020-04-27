from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        rounds = 0
        while candies:
            tmp = rounds * num_people + 1
            for i in range(num_people):
                if tmp + i <= candies:
                    ans[i] += (tmp + i)
                    candies -= (tmp + i)
                else:
                    ans[i] += candies
                    return ans
            rounds += 1


if __name__ == "__main__":
    s = Solution()
    print(s.distributeCandies(10, 3))