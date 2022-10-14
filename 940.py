class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # 不容怡计算到每个位置的不同子序列个数
        # 因为又要考虑选与不选又要考虑重复问题
        # 转为计算以每个字符结尾的不同子序列个数
        end = [0] * 26
        for c in s:
            end[ord(c) - ord('a')] = sum(end) + 1
        print(end)
        return sum(end) % (10**9 + 7)