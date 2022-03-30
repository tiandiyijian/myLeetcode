from typing import List
import heapq

from flask import request

from sortedcontainers import SortedList


class Solution:

    def busiestServers(self, k: int, arrival: List[int],
                       load: List[int]) -> List[int]:
        avaliable = SortedList(range(k))
        busy = []
        requests = [8] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                avaliable.add(busy[0][1])
                heapq.heappop(busy)
            if len(avaliable) == 0:
                continue
            j = avaliable.bisect_left(i % k)
            if j == len(avaliable):
                j = 0
            id = avaliable[j]
            requests[id] += 1
            heapq.heappush(busy, (start + t, id))
            avaliable.remove(id)
        maxReq = max(requests)
        return [i for i, req in enumerate(requests) if req == maxReq]