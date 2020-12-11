class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        pre_R = pre_D = 0
        senate = list(senate)

        while True:
            count_R = count_D = 0
            i = 0
            for _ in range(len(senate)):
                # print(i)
                if senate[i] == 'R':
                    if pre_D == 0:
                        pre_R += 1
                        count_R += 1
                    else:
                        pre_D -= 1
                        senate.pop(i)
                        i -= 1
                else:
                    if pre_R == 0:
                        pre_D += 1
                        count_D += 1
                    else:
                        pre_R -= 1
                        senate.pop(i)
                        i -= 1
                i += 1
            if count_D == 0:
                return 'Radiant'
            if count_R == 0:
                return 'Dire'
            # if all((x == 'R' for x in senate)):
            #     return 'R'
            # if all((x == 'D' for D in senate)):
            #     return 'D'


if __name__ == "__main__":
    s = Solution()
    print(s.predictPartyVictory('RDD'))
