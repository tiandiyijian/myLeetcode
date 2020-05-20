class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        idx_of_vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        counts = [[0] * 5 for _ in range(len(s)+1)]
        record = {'0' * 5: -1}
        ans = 0
        for i in range(len(s)):
            if not s[i] in idx_of_vowels:
                counts[i+1] = counts[i][:]
                key = ''.join([str(n) for n in counts[i+1]])
                # record.setdefault(key, i)
                if key in record:
                    ans = max(ans, i - record[key])
                else:
                    record[key] = i
            else:
                counts[i+1] = counts[i][:]
                idx = idx_of_vowels[s[i]]
                counts[i+1][idx] ^= 1
                key = ''.join([str(n) for n in counts[i+1]])
                # print(key)
                if key in record:
                    ans = max(ans, i - record[key])
                else:
                    record[key] = i
        # for i, c in enumerate(counts):
        #     if i > 0:
        #         print(s[i-1], end=' ')
        #     print(c)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findTheLongestSubstring("leetcodeisgreat"))
