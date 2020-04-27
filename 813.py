class Solution:
    def largestSumOfAverages(self, A: list, K: int) -> float:
        sums = [0] * len(A)
        sums[0] = A[0]
        for i in range(1, len(A)):
            sums[i] = sums[i-1] + A[i]
        dp = [[0.0]*(K+1) for i in range(len(A))]
        for k in range(1, K+1):
            for i in range(len(A)):
                if k == 1:
                    dp[i][k] = sums[i] / (i + 1)
                elif k > i + 1:
                    continue
                else:
                    for j in range(k - 1, i+1):
                        dp[i][k] = max(dp[i][k], dp[j-1][k-1] + (sums[i] - sums[j-1])/(i-j+1))
        print(dp)
        return dp[len(A)-1][K]

if __name__ == '__main__':
    s = Solution()
    A = [4,1,7,5,6,2,3]
    K = 4
    print(s.largestSumOfAverages(A, K))