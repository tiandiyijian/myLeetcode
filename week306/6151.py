class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # 不会
        def cnt(num_len, remove=0):
            ans = 1
            for i in range(num_len):
                ans *= (num_len-i)
            return ans
        
        s = str(n)
        l = list(s)
        ans = sum(cnt(num_len) for num_len in range(1, len(l)))

        def helper(l):
            ans = 0
            ans = (l[0] - 1) * cnt(len(l)-1, remove=1)

            