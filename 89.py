class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        ans = [0, 1]
        for i in range(1, n):
            pointer = value = pow(2, i)
            for j in range(pointer - 1, -1, -1):
                ans.append(ans[j] + value)
        return ans

    def grayCode1(self, n):
        ans = [0] * 2**n
        for i in range(1 << n):
            ans[i] = i ^ i>>1
        return ans

if __name__ == '__main__':
    a = Solution()
    print(a.grayCode1(2))