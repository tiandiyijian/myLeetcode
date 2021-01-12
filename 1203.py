import collections
from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def top_sort(degree, neighbors, items):
            q = collections.deque()
            for item in items:
                if degree[item] == 0:
                    q.append(item)

            res = []
            while q:
                u = q.popleft()
                res.append(u)
                for v in neighbors[u]:
                    degree[v] -= 1
                    if degree[v] == 0:
                        q.append(v)

            return res if len(res) == len(items) else []

        max_group_id = m
        for item in range(n):
            if group[item] == -1:
                group[item] = max_group_id
                max_group_id += 1

        item_degree = [0] * n
        group_degree = [0] * max_group_id
        item_neighbors = [[] for _ in range(n)]
        group_neighbors = [[] for _ in range(max_group_id)]
        group_to_items = [[] for _ in range(max_group_id)]

        for item in range(n):
            group_to_items[group[item]].append(item)
            for pre_item in beforeItems[item]:
                if group[pre_item] != group[item]:
                    # 不同组
                    group_degree[group[item]] += 1
                    group_neighbors[group[pre_item]].append(group[item])
                else:
                    # 同组
                    item_degree[item] += 1
                    item_neighbors[pre_item].append(item)

        # print(group_degree)
        ans = []
        group_order = top_sort(
            group_degree, group_neighbors, list(range(max_group_id)))
        if len(group_order) != max_group_id:
            return ans

        for group_id in group_order:
            item_order = top_sort(
                item_degree, item_neighbors, group_to_items[group_id])
            if len(item_order) != len(group_to_items[group_id]):
                return []
            ans += item_order
        return ans


if __name__ == "__main__":
    s = Solution()
    n = 8
    m = 2
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    before_items = [[], [6], [5], [6], [3, 6], [], [], []]
    print(s.sortItems(n, m, group, before_items))
