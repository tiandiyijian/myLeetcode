class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal) or n < 2:
            return False
        c1 = [0] * 26
        c2 = [0] * 26
        i = 0
        while i < n:
            c1[ord(s[i]) - ord('a')] += 1
            c2[ord(goal[i]) - ord('a')] += 1
            if s[i] != goal[i]:
                break
            i += 1
        # s = goal
        if i == n:
            return any(x >= 2 for x in c1)
        j = i + 1
        change_flag = False
        while j < n:
            c1[ord(s[j]) - ord('a')] += 1
            c2[ord(goal[j]) - ord('a')] += 1
            if s[j] != goal[j]:
                if not(s[i] == goal[j] and s[j] == goal[i]) or change_flag:
                    return False
                else:
                    change_flag = True
            j += 1
        return all(a == b for a, b in zip(c1, c2))
