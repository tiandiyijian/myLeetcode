from typing import List


_end = '_end'
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        ans = []
        trie = {}

        def add(word: str):
            current_dict = trie
            for c in word:
                current_dict = current_dict.setdefault(c, {})
            current_dict[_end] = True

        def check(word, start):
            if len(word) == start:
                return True
            current_dict = trie
            i = start
            # print(word)
            while i < len(word):
                # print(i, trie)
                # print(current_dict, word[i])
                if word[i] not in current_dict:
                    break
                current_dict = current_dict[word[i]]
                if _end in current_dict:
                    # print(word)
                    if check(word, i+1):
                        return True
                i += 1
            return False

        for word in words:
            i = 0
            if len(word) == 0:
                continue
            if check(word, 0):
                ans.append(word)
            else:
                add(word)
        return ans


words = ["cat", "cats", "catsdogcats", "dog",
         "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
print(Solution().findAllConcatenatedWordsInADict(words))
