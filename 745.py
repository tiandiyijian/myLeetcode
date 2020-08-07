from typing import List
from functools import lru_cache

_end = '_end_'
_index = '_index_'


class Trie:
    def __init__(self, *words):
        self.root = {}
        self.make_trie(*words)
        self.length = len(words)

    def make_trie(self, *words):
        root = self.root
        for idx, word in enumerate(words):
            current_dict = root
            for i in range(len(word)):
                current_dict = current_dict.setdefault(word[i], {})
                index = current_dict.setdefault(_index, [])
                index.append(idx)
            current_dict[_end] = True

    def in_trie(self, word):
        if not word:
            return range(self.length)
        current_dict = self.root
        for i in range(len(word)):
            current_dict = current_dict.get(word[i], None)
            if not current_dict:
                return []
        return current_dict.get(_index, [])

class ReverseTrie:
    def __init__(self, *words):
        self.root = {}
        self.make_trie(*words)
        self.length = len(words)

    def make_trie(self, *words):
        root = self.root
        for idx, word in enumerate(words):
            current_dict = root
            for i in range(len(word)-1, -1, -1):
                current_dict = current_dict.setdefault(word[i], {})
                index = current_dict.setdefault(_index, [])
                index.append(idx)
            current_dict[_end] = True

    def in_trie(self, word):
        if not word:
            return range(self.length)
        current_dict = self.root
        for i in range(len(word)-1, -1, -1):
            current_dict = current_dict.get(word[i], None)
            if not current_dict:
                return []
        return current_dict.get(_index, [])



class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie(*words)
        self.reverse_trie = ReverseTrie(*words)
        self.length = len(words)

    def f(self, prefix: str, suffix: str) -> int:
        index1 = self.trie.in_trie(prefix)
        # print(index1)
        if not index1:
            return -1
        index2 = self.reverse_trie.in_trie(suffix)
        if not index2:
            return -1
        i, j = len(index1) - 1, len(index2) - 1
        while i >= 0 and j >= 0:
            if index1[i] == index2[j]:
                return index1[i]
            elif index1[i] < index2[j]:
                j -= 1
            else:
                i -= 1
        return -1

if __name__ == "__main__":
    # Your WordFilter object will be instantiated and called as such:
    words = ["abbbababbb","baaabbabbb","abababbaaa","abbbbbbbba","bbbaabbbaa","ababbaabaa","baaaaabbbb","babbabbabb","ababaababb","bbabbababa"]
    prefix_suffix = [["","abaa"],["babbab",""],["ab","baaa"],["baaabba","b"],["abab","abbaabaa"],["","aa"],["","bba"],["","baaaaabbbb"],["ba","aabbbb"],["baaa","aabbabbb"]]
    obj = WordFilter(words)
    for p, s in prefix_suffix:
        print(obj.f(p, s))