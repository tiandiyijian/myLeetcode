from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        c0 = sum(typ == 0 for typ in students)
        c1 = n - c0

        for typ in sandwiches:
            if typ == 0 and c0 > 0:
                c0 -= 1
            elif typ == 1 and c1 > 0:
                c1 -= 1
            else:
                break

        return c1 + c0
