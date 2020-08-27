import collections
import heapq
from typing import List

"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        num_tickets = len(tickets)
        from_to = collections.defaultdict(list)

        for a, b in tickets:
            from_to[a].append(b)
        for key in from_to:
            from_to[key].sort()
        print(from_to)
        def dfs(path):
            print(path)
            if len(path) == num_tickets + 1:
                nonlocal ans
                if not ans:
                    ans = path[:]
                return
            
            nonlocal from_to
            if not from_to[path[-1]]:
                return
            
            locs = from_to[path[-1]][:]
            print(path, locs)
            for i, loc in enumerate(locs):
                if ans:
                    return
                del from_to[path[-1]][i]
                path.append(loc)
                dfs(path)
                path.pop()
                from_to[path[-1]].insert(i, loc)

        dfs(['JFK'])
        return ans
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(curr: str):
            # print(curr, stack)
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)
            # 逆序插入，最后再反转stack很关键，这样在递归的时候碰到的死胡同就被先入栈了
            # print(curr, stack)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])
        stack = list()
        dfs("JFK")
        return stack[::-1]


if __name__ == "__main__":
    s = Solution()
    t = [["JFK", "AAA"], ["JFK", "BBB"], ["BBB", "JFK"], ['AAA', 'JFK']]
    print(s.findItinerary(t))
