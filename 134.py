from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_gas = 0
        min_gas = float('inf')
        ans = 0
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            if current_gas < min_gas:
                min_gas = current_gas
                ans = i
        return (ans + 1) % len(gas) if current_gas >= 0 else -1


if __name__ == "__main__":
    s = Solution()
    print()
