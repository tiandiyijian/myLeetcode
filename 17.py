from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        lettersOfNums = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        for num in digits:
            num = int(num)
            if res == []:
                for letter in lettersOfNums[num]:
                    res.append(letter)
            else:
                temLen = len(res)
                for i in range(temLen):
                    for j in range(1, len(lettersOfNums[num])):
                        res.append(res[i] + lettersOfNums[num][j])
                    res[i] += lettersOfNums[num][0]
        return res
    
    def letterCombinations2(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_to_letter = {}
        for i in range(6):
            num_to_letter[str(i+2)] = [chr(ord('a') + j + 3 * i) for j in range(3)]
        num_to_letter['7'].append('s')
        num_to_letter['8'] = ['t', 'u', 'v']
        num_to_letter['9'] = ['w', 'x', 'y', 'z']
        ans = ['']
        for c in digits:
            ans = [a + b for a in ans for b in num_to_letter[c]]
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations2('23'))