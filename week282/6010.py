from typing import List
import math
import bisect


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        n = len(time)
        if n == 1:
            return time[0] * totalTrips
        maxfrac = math.gcd(time[0], time[1])
        minmul = time[0]*time[1] // maxfrac
        for t in time[2:]:
            # maxfrac = math.gcd(maxfrac, t)
            minmul = minmul // math.gcd(minmul, t) * t
        
        ans = 0
        loopTrip = sum(minmul // t for t in time)
        loops = totalTrips // loopTrip
        totalTrips %= loopTrip
        ans += loops * minmul

        ans += totalTrips * minmul / sum(time)
        return ans

        # print(maxfrac, minmul)

s = Solution()
time = [5,10,10]
trip = 9
print(s.minimumTime(time, trip))