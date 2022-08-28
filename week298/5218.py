class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        r = num % 10
        
        if k == 0:
            if r == 0:
                return 1
            else:
                return -1
        

        for i in range(1, 11):
            if (i * k) % 10 == r:
                if i * k <= num:
                    return i
                
        return -1


num, k = 58, 9
print(Solution().minimumNumbers(num, k))