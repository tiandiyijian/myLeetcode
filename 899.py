from typing import List


class Solution:
    # 简单证明k大于1时可以直接排序
    # 对于任意相邻的两个字符经过一轮操作可以交换它们的位置
    # 比如abdcef
    # abdcef -> dcefab -> efabcd -> abcdef
    # 交换了dc的位置
    # 既然任意相邻的字符可以交换位置那么就可以像冒泡排序一样排序了
    # 参考: https://leetcode.cn/problems/orderly-queue/solution/nao-jin-ji-zhuan-wan-by-heren1229-gg97/
    def orderlyQueue(self, s: str, k: int) -> str:
        return (
            min(s[i:] + s[:i] for i in range(len(s))) if k == 1 else ''.join(sorted(s))
        )
