class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # n = len(s)
        # for i in range(n):
        #     if s[i:] + s[0:i] == goal:
        #         return True
        # return False

        # 旋转数组特点
        return len(goal) == len(s) and goal in (s + s)