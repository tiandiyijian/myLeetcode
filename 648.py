from typing import List


class TrieNode:
    def __init__(self):
        self.data = [None] * 26
        self.end = False

    def add(self, word):
        cur = self
        for c in word:
            idx = ord(c) - ord("a")
            if cur.data[idx] is None:
                cur.data[idx] = TrieNode()
            cur = cur.data[idx]
        cur.end = True

    def find(self, word):
        cur = self
        for i, c in enumerate(word):
            idx = ord(c) - ord("a")
            if cur.data[idx] is not None:
                cur = cur.data[idx]
                if cur.end:
                    return word[: i + 1]
            else:
                return ""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieNode()
        for word in dictionary:
            trie.add(word)

        ans = []
        for word in sentence.split(" "):
            root = trie.find(word)
            ans.append(root if root else word)

        return " ".join(ans)


d = ["cat", "bat", "rat"]
s = "the cattle was rattled by the battery"
print(Solution().replaceWords(d, s))
