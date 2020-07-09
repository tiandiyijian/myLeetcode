from typing import List
from functools import lru_cache

from trie import Trie, _end


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        len_sentence = len(sentence)
        t = Trie()
        t.make_trie(*dictionary)
        # print(t.root)
        dp = list(range(len_sentence + 1))
        for i in range(1, len_sentence + 1):
            dp[i] = dp[i-1] + 1
            flag = False
            current_dict = t.root
            for j in range(i-1, -1, -1):
                current_dict = current_dict.get(sentence[j], None)
                if current_dict is None:
                    break
                elif current_dict.get(_end, False):
                    dp[i] = min(dp[i], dp[j])
        # print(dp)
        return dp[len_sentence]

    def respace1(self, dictionary: List[str], sentence: str) -> int:
        len_sentence = len(sentence)
        dictionary = set(dictionary)
        @lru_cache(maxsize=1000)
        def helper(start):
            s = start
            if start == len_sentence:
                return 0
            ans = len_sentence - start
            for i in range(start + 1, len_sentence + 1):
                if sentence[start: i] in dictionary:
                    ans = min(helper(i), ans)
            if sentence[s] not in dictionary:
                return min(ans, 1 + helper(start+1))
            return ans
        return helper(0)


if __name__ == "__main__":
    s = Solution()
    dictionary = ["looked", "just", "like", "her", "brother"]
    sentence = "jesslookedjustliketimherbrother"
    print(s.respace(dictionary, sentence))
