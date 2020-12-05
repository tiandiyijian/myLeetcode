from collections import Counter
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        if not tasks:
            return 0

        q = []
        for count in Counter(tasks).values():
            heapq.heappush(q, -count)
        # print(q)
        time = 0
        while q:
            # print(q)
            if (current_len := len(q)) <= n + 1:
                new_q = [count + 1 for count in q if count < -1]
                
                if new_q:
                    heapq.heapify(new_q)
                    q = new_q
                    time += n + 1
                else:
                    time += current_len
                    return time
            else:
                buffer = []
                for i in range(n + 1):
                    tmp = heapq.heappop(q)
                    if tmp < -1:
                        buffer.append(tmp + 1)
                for count in buffer:
                    heapq.heappush(q, count)
                time += n + 1
        return time

    def leastInterval2(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks).values()
        max_count = max(counter)
        num_max_count_task = sum(1 for c in counter if c == max_count)
        return max(((n + 1)*(max_count - 1) + num_max_count_task), len(tasks))

if __name__ == "__main__":
    s = Solution()
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    print(s.leastInterval2(tasks, 2))
