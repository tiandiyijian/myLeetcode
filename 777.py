class Solution:
    # 忽略'X'的话start和end中'L'和'R'的组成的子序列是一样的
    # start中的L必须在end中L的右边，R必须在左边
    # 所以其实只需要判断L和R的下标是否满足要求即可
    # 我这种写法相当于是看见不一样的就判断移动之后能否变成一样的
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)

        i = 0
        while i < n:
            if start[i] == end[i]:
                i += 1
                continue
            if start[i] != 'X' and end[i] != 'X':
                return False
            if start[i] == 'L':
                return False
            cnt1 = cnt2 = 0
            tar = ''
            if start[i] == 'R':
                cnt1 = 1
                tar = 'R'
            else:
                cnt2 = 1
                tar = 'L'
            for j in range(i + 1, n):
                if (start[j] != tar and start[j] != 'X') or (
                    end[j] != tar and end[j] != 'X'
                ):
                    return False

                if start[j] == tar:
                    cnt1 += 1
                if end[j] == tar:
                    cnt2 += 1

                if cnt1 == cnt2:
                    break
            else:
                return False
            i = j + 1

        return True
