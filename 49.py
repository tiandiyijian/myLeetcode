from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def str2str(s):
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            return tuple(chars)

        dt = defaultdict(list)
        for s in strs:
            dt[str2str(s)].append(s)
        # ans = [l for l in dt.values()]
        # return ans
        return list(dt.values())


if __name__ == "__main__":
    s = Solution()
    print()
