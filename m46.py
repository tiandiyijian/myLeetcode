class Solution:
    def translateNum(self, num: int) -> int:
        pre, cur = 1, 1
        num = [int(x) for x in str(num)]
        for i in range(1, len(num)):
            if num[i-1] > 0 and num[i] + num[i-1] * 10 < 26:
                pre, cur = cur, pre + cur
            else:
                pre = cur
                # cur = cur
        return cur

if __name__ == "__main__":
    s = Solution()
    print(s.translateNum(18822))