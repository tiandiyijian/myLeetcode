from sortedcontainers import SortedDict


class MyCalendarTwo:
    def __init__(self):
        self.cnter = SortedDict()

    def book(self, start: int, end: int) -> bool:
        cnter = self.cnter
        cnter[start] = cnter.get(start, 0) + 1
        cnter[end] = cnter.get(end, 0) - 1

        maxBook = 0
        for k in cnter.keys():
            maxBook += cnter[k]
            if maxBook > 2:
                cnter[start] -= 1
                cnter[end] += 1
                return False
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
