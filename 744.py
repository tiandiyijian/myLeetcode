from bisect import bisect_right
from typing import List


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target
                                    ) if letters[-1] > target else 0]
