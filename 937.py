from typing import List


class Solution:

    def reorderLogFiles1(self, logs: List[str]) -> List[str]:
        letterLog = []
        numLog = []

        for log in logs:
            if log[-1].isdigit():
                numLog.append(log)
            else:
                letterLog.append(log)

        letterLog.sort(key=lambda x: (x[x.find(' ') + 1:], x[:x.find(' ')]))

        return letterLog + numLog

    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def order(log: str):
            a, b = log.split(' ', 1)
            return (0, b, a) if b[0].isalpha() else (1, )

        return sorted(logs, key=order)


logs = [
    "dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig",
    "let3 art zero"
]
print(Solution().reorderLogFiles(logs))