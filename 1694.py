class Solution:
    def reformatNumber(self, number: str) -> str:
        num = number.replace(' ', '').replace('-', '')
        sz = len(num)
        if sz <= 3:
            return num
        if sz == 4:
            return num[:2] + '-' + num[2:]

        match sz % 3:
            case 0:
                return '-'.join(num[i * 3 : i * 3 + 3] for i in range(sz // 3))
            case 1:
                return '-'.join(
                    num[i * 3 : i * 3 + 3] for i in range(sz // 3 - 1)
                ) + '-'.join(['', num[-4:-2], num[-2:]])
            case 2:
                return (
                    '-'.join(num[i * 3 : i * 3 + 3] for i in range(sz // 3))
                    + '-'
                    + num[-2:]
                )
