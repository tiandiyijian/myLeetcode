class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max((num[i:i+3] for i in range(len(num)-2) if num[i] == num[i+1] and num[i] == num[i+2]), default="")