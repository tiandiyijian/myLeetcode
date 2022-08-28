from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.cur_list = deque()
        self.cur_sum = 0


    def next(self, val: int) -> float:
        l = self.cur_list
        if len(l) < self.size:
            l.append(val)
            self.cur_sum += val
            return self.cur_sum / len(l)
        else:
            l.append(val)
            self.cur_sum += val - l.popleft()
            return self.cur_sum / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)