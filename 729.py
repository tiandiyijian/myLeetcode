from sortedcontainers import SortedDict


class MyCalendar:
    def __init__(self):
        self.dates = SortedDict()

    def book(self, start: int, end: int) -> bool:
        dates = self.dates

        if not dates:
            dates[start] = end
            return True
        # print(dates, start, end)
        x = dates.bisect_right(start)
        if x != 0:
            if dates.values()[x - 1] <= start and (
                x == len(dates) or dates.keys()[x] >= end
            ):
                dates[start] = end
                return True
            return False

        if dates.keys()[0] >= end:
            dates[start] = end
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
