class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        n1, n2 = len(first), len(second)
        if n1 == n2:
            return sum(a != b for a, b in zip(first, second)) <= 1
        
        if n1 > n2:
            n1, n2 = n2, n1
            first, second = second, first
        
        i1 = i2 = 0
        edit = False
        while i2 < n2:
            if first[i1] != second[i2]:
                if edit:
                    return False
                edit = True
                i2 += 1
            else:
                i1 += 1
                i2 += 1
        
        return True
        