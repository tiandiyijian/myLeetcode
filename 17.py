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