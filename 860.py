from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 写完了才发现面值只有5、10、20
        dollar_idx = {
            100: 4,
            50: 3,
            20: 2,
            10: 1,
            5: 0
        }

        dollar = [
            [5, 0],
            [10, 0],
            [20, 0],
            [50, 0],
            [100, 0]
        ]

        for bill in bills:
            if bill == 5:
                dollar[0][1] += 1
            else:
                if dollar[0][1] == 0:
                    return False
                idx = dollar_idx[bill]
                dollar[idx][1] += 1
                money = bill - 5

                for i in range(idx - 1, -1, -1):
                    count = min(money // dollar[i][0], dollar[i][1])
                    money -= count * dollar[i][0]
                    dollar[i][1] -= count
                if money > 0:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print()
