from collections import defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        neighbors = defaultdict(list)
        for [a, b] in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        ans = [0] * n
        visited = [False] * n

        def dfs(root):
            label_count = defaultdict(int)
            label_count[labels[root]] = 1
            visited[root] = True
            for node in neighbors[root]:
                if not visited[node]:
                    tmp_count = dfs(node)
                    for label, count in tmp_count.items():
                        label_count[label] += count
            ans[root] = label_count[labels[root]]
            return label_count

        dfs(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
