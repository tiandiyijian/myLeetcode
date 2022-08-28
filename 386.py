from typing import List


class Solution:

    def lexicalOrder1(self, n: int) -> List[int]:
        ans = []

        def helper(i):
            # print(i)
            if i > n:
                return
            ans.append(i)
            new_i = i * 10
            for x in range(new_i, new_i + 10):
                helper(x)

        def helper1(prefix):
            # 和440不一样
            # 这种做法是一下子将一层(位数一样)的数字全都添加进去, 再考虑下一层
            # 但这样就不是字典序了
            # 440是求某一个前缀的大小, 可以用这种思路
            next = prefix + 1
            while prefix <= n:
                ans.extend(range(prefix, min(n + 1, next)))
                prefix *= 10
                next *= 10
                print(ans)

        for i in range(1, 10):
            helper(i)

        return ans

    def lexicalOrder(self, n: int) -> List[int]:
        # 直接模拟
        # 空间复杂度为O(1)
        ans = [0] * n
        num = 1
        for i in range(n):
            ans[i] = num
            num *= 10
            if num > n:
                while num >= n or num % 10 == 9:
                    # 如果num=n那么num+1就超出范围了
                    # 如果num最后一位是9那么它应该继续回退
                    # 比如说19之后应该是2而不是20
                    num //= 10
                num += 1
        return ans



# print(Solution().lexicalOrder(13))
# print(Solution().lexicalOrder(2))
print(Solution().lexicalOrder(100))