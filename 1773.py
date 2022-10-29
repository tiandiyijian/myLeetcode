from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        match ruleKey:
            case 'type':
                idx = 0
            case 'color':
                idx = 1
            case _:
                idx = 2
        return sum(item[idx] == ruleValue for item in items)
