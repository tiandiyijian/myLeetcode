from heapq import heappop, heappush
from typing import List


class Solution:
    def minRefuelStops0(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        n = len(stations)
        ans, fuel, prev, h = 0, startFuel, 0, []
        for i in range(n + 1):
            curr = stations[i][0] if i < n else target
            fuel -= curr - prev
            while fuel < 0 and h:
                fuel -= heappop(h)
                ans += 1
            if fuel < 0:
                return -1
            if i < n:
                heappush(h, -stations[i][1])
                prev = curr
        return ans

    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        # 可以理解为路过加油站的时候可以先不加油只是记录下来
        # 等到没油的时候再从之前路过的加油站里选择油最多的那个

        loc = 0
        ans = 0
        remain = startFuel
        q = []
        idx = 0
        n = len(stations)

        while loc < target:
            if remain == 0:
                if q:
                    remain = -heappop(q)
                    ans += 1
                else:
                    return -1
            loc += remain
            remain = 0
            while idx < n and stations[idx][0] <= loc:
                heappush(q, -stations[idx][1])
                idx += 1

        return ans
