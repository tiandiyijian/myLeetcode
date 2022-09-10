from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            match log:
                case '../':
                    ans = max(ans-1, 0)
                case './':
                    pass
                case _:
                    ans += 1
        return ans
                        