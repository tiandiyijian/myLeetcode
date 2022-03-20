class Solution:
    def countCollisions(self, directions: str) -> int:
        # d = list(directions)
        # n = len(d)
        # ans = 0
        # while True:
        #     cur = 0
        #     for i in range(n):
        #         if d[i] == 'R' and i + 1 < n:
        #             if d[i+1] == 'L':
        #                 cur += 2
        #                 d[i] = 'S'
        #                 d[i+1] = 'S'
        #             elif d[i+1] == 'S':
        #                 cur += 1
        #                 d[i] = 'S'
        #         elif d[i] == 'S':
        #             if i+1 < n and d[i+1] == 'L':
        #                 cur += 1
        #                 d[i+1] = 'S'
        #     # print(d, cur)
        #     if cur == 0:
        #         return ans
        #     ans += cur
        
        # 其实可以更简单的，只要判断R的右边有没有S或L和L的左边有没有S或R即可
        n = len(directions)
        leftR = n
        for i in range(n):
            if directions[i] == 'R':
                leftR = i
                break
        rightL = -1
        for i in range(n-1, -1, -1):
            if directions[i] == 'L':
                rightL = i
                break

        ans = 0
        if leftR > rightL:
            for i in range(leftR):
                if directions[i] == 'S':
                    ans += sum(1 for j in range(i, leftR) if directions[j] == 'L')
                    break
            for i in range(n-1, rightL, -1):
                if directions[i] == 'S':
                    ans += sum(1 for j in range(i, rightL, -1) if directions[j] == 'R')
                    break
        else:
            ans = sum(1 for j in range(leftR, rightL+1) if directions[j] != 'S')
            for i in range(leftR):
                if directions[i] == 'S':
                    ans += sum(1 for j in range(i, leftR) if directions[j] == 'L')
                    break
            for i in range(n-1, rightL, -1):
                if directions[i] == 'S':
                    ans += sum(1 for j in range(i, rightL, -1) if directions[j] == 'R')
                    break
        return ans


d = "RSS"
print(len(d))
print(Solution().countCollisions(d))