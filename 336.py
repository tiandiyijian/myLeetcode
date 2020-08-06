from typing import List

_end = '_end_'
_index = '_index_'


class Trie:
    def __init__(self):
        self.root = {}

    def make_trie(self, *words):
        root = self.root
        for i, word in enumerate(words):
            current_dict = root
            for j in range(len(word)):
                current_dict = current_dict.setdefault(word[j], {})
            current_dict[_end] = True
            current_dict[_index] = i

    def in_trie(self, word, left, right):
        current_dict = self.root
        for i in range(right, left - 1, -1):
            current_dict = current_dict.get(word[i], None)
            if not current_dict:
                return -1
        return current_dict.get(_index, -1)


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 如果两个单词可以构成回文子串
        # 那么肯定是一个单词的前缀或者后缀(空串也算)本身是回文串
        # 并且这个单词剩余的另一部分和另外一个单词字母顺序正好相反
        def isPalindrome(word, left, right):
            length = right - left + 1
            return length < 0 or all([word[left + i] == word[right - i] for i in range(length // 2)])

        trie = Trie()
        trie.make_trie(*words)
        # print(trie.root)
        ans = []
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if j and isPalindrome(word, 0, j - 1):
                    right_id = trie.in_trie(word, j, m - 1)
                    if right_id != -1 and right_id != i:
                        ans.append([right_id, i])
                if isPalindrome(word, j, m - 1):
                    left_id = trie.in_trie(word, 0, j - 1)
                    if left_id != -1 and left_id != i:
                        ans.append([i, left_id])
        return ans


if __name__ == "__main__":
    s = Solution()
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    print(s.palindromePairs(words))
