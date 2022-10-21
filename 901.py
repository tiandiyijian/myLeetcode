class StockSpanner:
    def __init__(self):
        self.idx = 0
        self.prices = [(0, 10**5 + 1)]

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.prices[-1][1]:
            self.prices.pop()
        ans = self.idx - self.prices[-1][0]
        self.prices.append((self.idx, price))
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
