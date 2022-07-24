from typing import List


class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        if start < destination:
            start, destination = destination, start

        path1 = 0
        for i in range(start, destination):
            path1 += distance[i]

        path2 = sum(distance) - path1

        return min(path1, path2)
