class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for d in moves:
            if d == 'R':
                x += 1
            elif d == 'L':
                x -= 1
            elif d == 'U':
                y += 1
            else:
                y -= 1
        return x == 0 and y == 0


if __name__ == "__main__":
    s = Solution()
    print(s.judgeCircle('LRUD'))
