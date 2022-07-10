class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(target)
        i = 0

        for j, c in enumerate(target):
            if c == '_':
                continue
        
            while i < n and start[i] == '_':
                i += 1

            if i == n:
                return False

            # print(i, j)
            if c != start[i]:
                return False
            
            if c == 'L':
                if i < j:
                    return False
            
            if c == 'R':
                if i > j:
                    return False
            
            i += 1
        
        while i < n and start[i] == '_':
            i += 1

        return i == n


start = "_L__R__R_"
target = "L______RR"

start = "R_L_"
target = "__LR"

start = "_R"
target = "R_"

start = "_L__R__R_L"
target = "L______RR_"
print(Solution().canChange(start, target))

            
        