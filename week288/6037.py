class Solution:
    def largestInteger(self, num: int) -> int:
        odds = []
        evens = []
        isOdd = []
        while num > 0:
            tmp = num % 10
            num //= 10
            if tmp & 1 == 1:
                odds.append(tmp)
                isOdd.append(True)
            else:
                evens.append(tmp)
                isOdd.append(False)
        
        isOdd = isOdd[::-1]
        odds.sort(reverse=True)
        evens.sort(reverse=True)
        i = j = 0
        ans = 0
        for Odd in isOdd:
            if Odd:
                ans = ans * 10 + odds[i]
                i += 1
            else:
                ans = ans * 10 + evens[j]
                j += 1
        return ans

print(Solution().largestInteger(65875))
