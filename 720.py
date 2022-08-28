from typing import List

class Solution:
    def longestWord2(self, words: List[str]) -> str:
        root = {}
        _end = '_end'
        def add2root(word):
            cur_root = root
            flag = True
            for c in word[:-1]:
                cur_root = cur_root.setdefault(c, {})
                # 必须从单个字母开始
                if _end not in cur_root:
                    flag = False
            cur_root = cur_root.setdefault(word[-1], {})
            cur_root[_end] = _end
            return len(word) if flag else 0
        
        ans = ''
        words.sort()
        for w in words:
            size = add2root(w)
            if size > len(ans):
                ans = w
        
        return ans

    def longestWord(self, words: List[str]) -> str:
        root = {}
        _end = '_end'
        def add2root(word):
            cur_root = root
            for c in word:
                cur_root = cur_root.setdefault(c, {})
            cur_root[_end] = _end
        
        def search(word):
            cur_root = root
            for c in word:
                if c not in cur_root:
                    return False
                cur_root = cur_root[c]
                if _end not in cur_root:
                    return False
            return True
        
        for w in words:
            add2root(w)
        
        ans = ''
        for w in words:
            if search(w) and (len(w) > len(ans) or (len(w) == len(ans) and w < ans)):
                ans = w
        
        return ans
