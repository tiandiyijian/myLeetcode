from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = [pow(a ** 2 + b ** 2, 0.5) for a, b in points]
        max_heap = [len(dis) - 1] * K
        dis.append(float('inf'))

        def max_heapify(i):
            l = (i << 1) + 1
            r = l + 1
            largest = i
            if l < K and dis[max_heap[l]] > dis[max_heap[i]]:
                largest = l
            if r < K and dis[max_heap[r]] > dis[max_heap[largest]]:
                largest = r
            if largest != i:
                max_heap[i], max_heap[largest] = max_heap[largest], max_heap[i]
                max_heapify(largest)

        for i in range(len(points)):
            d = dis[i]
            if d < dis[max_heap[0]]:
                max_heap[0] = i
                max_heapify(0)
                print(max_heap)

        ans = []
        for idx in max_heap:
            ans.append(points[idx])

        return ans
        

if __name__ == "__main__":
    s = Solution()
    points = [[1,3],[-2,2],[2,-2]]
    K = 2
    print(s.kClosest(points, K))