from bisect import bisect_left


class RecentCounter:

    def __init__(self):
        # self.cnt = 0
        self.l = []

    def ping(self, t: int) -> int:
        if self.l and self.l[0] >= t - 3000:
            self.l.append(t)
            return len(self.l)

        idx = bisect_left(self.l, t - 3000)
        self.l = self.l[idx:]

        self.l.append(t)
        return len(self.l)