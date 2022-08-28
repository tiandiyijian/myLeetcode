from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        row = 1
        left = 100
        for c in s:
            width = widths[ord(c)-ord('a')]
            if width > left:
                row += 1
                left = 100 - width
            else:
                left -= width
        return [row, 100-left]