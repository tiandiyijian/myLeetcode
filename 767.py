from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = Counter(S)
        heap = []
        for key, val in counter.items():
            heap.append((-val, key))
        heapq.heapify(heap)
        ans = ''
        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            ans += char1 + char2
            if count1 < -1:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 < -1:
                heapq.heappush(heap, (count2 + 1, char2))
        # print(heap)
        if heap:
            if heap[0][0] < -1:
                return ''
            else:
                return ans + heap[0][1]
        else:
            return ans
        

if __name__ == "__main__":
    s = Solution()
    S = 'aaabc'
    print(s.reorganizeString(S))
