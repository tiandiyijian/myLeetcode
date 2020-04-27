class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # sum = m + n - 2
        # return (int)(self.jiecheng(sum) / (self.jiecheng(m-1) * self.jiecheng(n-1)))
        if m > n:
            m, n = n, m
        sum_of_steps = m + n - 2
        numerator = 1
        denominator = 1
        for i in range(1, m):
            numerator *= sum_of_steps
            sum_of_steps -= 1
            denominator *= i
        return numerator // denominator
            

    def jiecheng(self, x):
        if x == 0:
            return 1
        res = x
        while x > 2:
            x -= 1
            res *= x
        return res
