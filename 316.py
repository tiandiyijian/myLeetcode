from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        exist = [False] * 26
        left = Counter(s)
        stack = []

        for ch in s:
            if not exist[ord(ch) - ord('a')]:
                while stack and stack[-1] > ch and left[stack[-1]]:
                    exist[ord(stack[-1]) - ord('a')] = False
                    stack.pop()
                stack.append(ch)
                left[ch] -= 1
                exist[ord(ch) - ord('a')] = True
            else:
                left[ch] -= 1

        return ''.join(stack)


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicateLetters('bcabc'))
