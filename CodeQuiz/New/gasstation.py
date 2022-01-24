class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        ref = []
        n = len(gas)
        for i in range(n):
            ref.append(gas[i] - cost[i])
        print(ref)
        for start in range(n):
            tot = 0
            pointer = 0
            while pointer < n:
                idx = (start + pointer)%n
                tot += ref[idx]
                if tot < 0:
                    break
                if pointer == n - 1:
                    return start
                pointer += 1
        return -1
        """

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start

mySolution = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(mySolution.canCompleteCircuit(gas, cost))