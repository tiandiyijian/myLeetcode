from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap = [float('-inf')] * k
        self._heap_size = 0
        self._k = k
        for i in range(0, min(k, len(nums))):
            self._heap[i] = nums[i]
            self.percolateUp(i)
            self._heap_size += 1

        for i in range(k, len(nums)):
            if nums[i] > self._heap[0]:
                self._heap[0] = nums[i]
                self.percolateDown(self._heap_size, 0)
        # print(self._heap)

    def add(self, val: int) -> int:
        if self._heap_size < self._k:
            self._heap[self._heap_size] = val
            self.percolateUp(self._heap_size)
            self._heap_size += 1
        elif val > self._heap[0]:
            self._heap[0] = val
            self.percolateDown(self._heap_size, 0)
        return self._heap[0]

    def percolateDown(self, n, i):
        while i < n >> 1:
            left = (i << 1) + 1
            right = left + 1
            smallest = i
            if self._heap[i] > self._heap[left]:
                smallest = left
            if right < self._heap_size and self._heap[smallest] > self._heap[right]:
                smallest = right
            if smallest != i:
                self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
                i = smallest
            else:
                break

    def percolateUp(self, i):
        while i > 0:
            parent = (i - 1) >> 1
            if self._heap[i] < self._heap[parent]:
                self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
                i = parent
            else:
                break


if __name__ == "__main__":
    nums = [0]
    obj = KthLargest(2, nums)
    print(obj.add(-1))
    print(obj.add(1))
    print(obj.add(-2))
    print(obj.add(-4))
    print(obj.add(3))
