from collections import defaultdict
from typing import List


class MagicDictionary:
    def __init__(self):
        self.dict = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        d = self.dict
        for word in dictionary:
            for i in range(len(word)):
                d[word[:i] + '*' + word[i + 1 :]].add(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            if (
                s := self.dict.get(searchWord[:i] + "*" + searchWord[i + 1 :])
            ) is not None:
                if len(s) > 1 or searchWord not in s:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
