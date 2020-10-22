from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        length = len(S)
        ans = []
        i = 0
        while i < length:
            j = S.rfind(S[i])
            if j == -1 or j == i:
                ans.append(1)
                i += 1
                continue
            r = j
            k = i + 1
            while k < r:
                tmp = S.rfind(S[k])
                if tmp > r:
                    r = tmp
                k += 1
            ans.append(r - i + 1)
            i = r + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
