from collections import Counter


class FreqStack:
    def __init__(self):
        self.freqs = Counter()
        self.stks = []

    def push(self, val: int) -> None:
        cnt = self.freqs[val]
        self.freqs[val] = cnt + 1

        if cnt == len(self.stks):
            self.stks.append([])
        self.stks[cnt].append(val)

    def pop(self) -> int:
        val = self.stks[-1].pop()
        self.freqs[val] -= 1

        if not self.stks[-1]:
            self.stks.pop()

        return val
