from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 关键在于怎么找单词的邻居，如果直接建图的话会很耗时
        # 因为单词的邻居最多就只有 len(word) * 26 种可能，当单词很多时这样寻找邻居反而更高效
        wordSet = set(wordList)
        if endWord not in wordSet or beginWord == endWord:
            return 0
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        visited = {beginWord}
        q = deque()
        q.append(beginWord)
        length = 1
        while q:
            q_len = len(q)
            for _ in range(q_len):
                current_word = q.popleft()
                word_list = list(current_word)
                for i in range(len(word_list)):
                    tmp_char = word_list[i]
                    for j in range(26):
                        word_list[i] = chr(ord('a') + j)
                        new_word = ''.join(word_list)
                        if new_word in wordSet:
                            if new_word == endWord:
                                return length + 1
                            elif new_word not in visited:
                                q.append(new_word)
                                visited.add(new_word)
                    word_list[i] = tmp_char
            length += 1
        return 0


if __name__ == "__main__":
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(s.ladderLength(beginWord, endWord, wordList))
