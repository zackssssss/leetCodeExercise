from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalgas = 0
        totalcost = 0
        for i in range(len(gas)):
            totalgas += gas[i]
            totalcost += cost[i]
        if totalcost > totalgas:
            return -1

        currgas = 0
        start = 0
        for i in range(len(gas)):
            currgas += gas[i] - cost[i]
            if currgas < 0:
                currgas = 0
                start = i + 1
        return start


if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    s = Solution()
    print(s.canCompleteCircuit(gas, cost))
