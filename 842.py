from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        L = len(S)

        for l1 in range(1, L // 2 + 1):
            first = int(S[:l1])
            if first > 2**31 - 1:
                break
            for l2 in range(1, L // 2 + 1):
                second = int(S[l1:l1+l2])
                if second > 2**31 - 1:
                    break
                ans = [first, second]
                start = l1 + l2
                while start < L:
                    num = ans[-1] + ans[-2]
                    if (num := ans[-1] + ans[-2]) > 2**31 - 1:
                        break
                    tmp = str(num)
                    tmp_len = len(tmp)
                    if start + tmp_len <= L and S[start:start+tmp_len] == tmp:
                        start += tmp_len
                        ans.append(num)
                    else:
                        break
                if start == L and len(ans) > 2:
                    return ans
                if S[l1] == '0':
                    break
            if S[0] == '0':
                break
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.splitIntoFibonacci('1123'))
