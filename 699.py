from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        pos = set()
        for p, l in positions:
            pos.add(p)
            pos.add(p+l-1)
        
        idx_map = {v:i for i, v in enumerate(sorted(pos))}
        records = [0] * len(idx_map)
        
        ans = []
        cur = 0
        for p, l in positions:
            left, right = idx_map[p], idx_map[p+l-1]
            new_height = max(records[left:right+1]) + l
            for i in range(left, right+1):
                records[i] = new_height
            cur = max(cur, new_height)
            ans.append(cur)
        return ans
        