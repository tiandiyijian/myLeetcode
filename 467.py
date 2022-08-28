class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # 我只想到了求以每个字母为开头的子串的最大长度, 但这样不好算(好像倒着遍历就一样了)
        # 但是没想到求以每个字母为结尾的子串的最大长度, 这样就很好算了
        n = len(p)
        count = [0] * 26
        i = 0
        while i < n:
            j = i + 1
            ii = i
            while j < n and (
                (p[i] < "z" and ord(p[i]) + 1 == ord(p[j]))
                or (p[i] == "z" and p[j] == "a")
            ):
                count[ord(p[i]) - 97] = max(count[ord(p[i]) - 97], j - ii)
                i += 1
                j += 1
            count[ord(p[i]) - 97] = max(count[ord(p[i]) - 97], j - ii)
            i = j
        return sum(count)
