class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        if i < len(name):
            return False
        elif j < len(typed):
            for k in range(j, len(typed)):
                if typed[k] != name[-1]:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    print()
