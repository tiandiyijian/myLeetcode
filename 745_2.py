from typing import List


class TrieNode:
    def __init__(self, idx=-1):
        self.children = [None] * 27
        self.idx = idx

# 又有前缀又有后缀这种就可以考虑拼接
# 还可以让字典树的 key 是前缀字符和后缀字符的组合
# 发现我第一次写的思路也可以, 构造前缀后缀两个字典树, 然后从大到小比较索引, 如果有相等的就找到答案了
class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()

        def add(word, idx):
            cur = self.root
            for c in word:
                if cur.children[ord(c) - ord('a')] is None:
                    cur.children[ord(c) - ord('a')] = TrieNode(idx)
                cur = cur.children[ord(c) - ord('a')]

        for idx in range(len(words) - 1, -1, -1):
            for i in range(len(words[idx])):
                add(words[idx][i:] + '{' + words[idx], idx)

        # print(self.root)

    def f(self, pref: str, suff: str) -> int:
        tar = suff + '{' + pref
        cur = self.root
        for c in tar:
            if cur.children[ord(c) - ord('a')] is None:
                return -1
            cur = cur.children[ord(c) - ord('a')]
        return cur.idx


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
