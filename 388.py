from collections import deque


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        items = input.split('\n')
        s = deque([])
        max_len = 0
        for item in items:
            size = len(item)
            for i in range(size):
                if item[i] != '\t':
                    break
            while s and s[-1][0] >= i:
                s.pop()
            if '.' not in item:
                s.append((i, size-i + (s[-1][1] + 1 if s else 0)))
            else:
                max_len = max(max_len, size - i + (s[-1][1] + 1 if s else 0))
        return max_len



input = 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
input = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
input = 'a'
input = 'file1.txt\nfile2.txt\nlongfile.txt'
print(Solution().lengthLongestPath(input))