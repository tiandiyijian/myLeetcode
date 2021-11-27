class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self) -> List[int]:
        self.total -= 1
        x = random.randint(0, self.total)
        # 查找位置 x 对应的映射
        idx = self.map.get(x, x)
        # 将位置 x 对应的映射设置为位置 total 对应的映射
        self.map[x] = self.map.get(self.total, self.total)
        return [idx // self.n, idx % self.n]
        
    def reset(self) -> None:
        self.total = self.m * self.n
        self.map.clear()




# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()