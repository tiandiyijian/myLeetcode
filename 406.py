from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(x[0], -x[1]))
        indices = list(range(len(people)))
        ans = [None] * len(people)
        for h, k in people:
            # print(h, k, indices)
            ans[indices[k]] = [h, k]
            indices.pop(k)
        return ans


if __name__ == "__main__":
    s = Solution()
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(s.reconstructQueue(people))