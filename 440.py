

class Node:
    def __init__(self) -> None:
        self.children = [None] * 10
        self.cnt = 0

    def __str__(self) -> str:
        return str(list(chr(i + ord('0')) for i in range(10) if self.children[i]))


class Solution:
    def findKthNumber2(self, n: int, k: int) -> int:
        # 被字典树这个标签给骗了-_-
        # 不过好歹输出的答案是对的-_-
        root = Node()
        for i in range(1, n+1):
            s = str(i)
            node = root
            node.cnt += 1
            for c in s:
                # print(c)
                if (tmp := node.children[ord(c) - ord('0')]) is not None:
                    node = tmp
                else:
                    new_node = Node()
                    node.children[ord(c) - ord('0')] = new_node
                    node = new_node
                node.cnt += 1
        node = root
        ans = ''
        while True:
            pre_cnt = 0
            for i in range(10):
                if node.children[i] is None:
                    continue
                cur_cnt = node.children[i].cnt + pre_cnt
                if k <= cur_cnt:
                    k -= pre_cnt
                    ans += chr(i + ord('0'))
                    if k == 1:
                        return int(ans)
                    k -= 1
                    node = node.children[i]
                    break
                pre_cnt = cur_cnt

    def findKthNumber(self, n: int, k: int) -> int:
        def getSize(prefix: int):
            next = prefix + 1
            cnt = 0
            while prefix <= n:
                cnt += min(n+1, next) - prefix
                prefix *= 10
                next *= 10
            return cnt
        
        p = 1
        prefix = 1
        while p < k:
            cnt = getSize(prefix)
            if p + cnt > k:
                prefix *= 10
                p += 1
            else:
                p += cnt
                prefix += 1
        return prefix

print(Solution().findKthNumber(4289384, 1922239))
print(Solution().findKthNumber2(4289384, 1922239))