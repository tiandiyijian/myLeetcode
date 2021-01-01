from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 统计两朵花之间可以种植的花的数量
        count, m, prev_flower = 0, len(flowerbed), -1
        for i in range(m):
            if flowerbed[i] == 1:
                if prev_flower < 0:
                    count += i // 2
                else:
                    count += (i - prev_flower - 2) // 2
                if count >= n:
                    return True
                prev_flower = i

        if prev_flower < 0:
            count += (m + 1) // 2
        else:
            count += (m - prev_flower - 1) // 2

        return count >= n


if __name__ == "__main__":
    s = Solution()
    print()
