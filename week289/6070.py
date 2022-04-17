class Solution:

    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ''
            for i in range(len(s) // k + (1 if len(s) % k else 0)):
                new_s += str(sum(int(c) for c in s[i * k:(i + 1) * k]))
                # print(new_s)
            s = new_s
        return s


print(Solution().digitSum("1234", 2))
