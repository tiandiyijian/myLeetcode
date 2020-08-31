import collections
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        q = collections.deque()
        q.append(0)
        visited[0] = 1
        while q:
            room = q.popleft()
            for i in rooms[room]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
        return sum(visited) == len(visited)


if __name__ == "__main__":
    s = Solution()
    print()
