class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # ans=0
        # curr=0

        # for i in range(len(gas)):
        #     curr+=gas[i]-cost[i]

        if sum(gas)<sum(cost):
            return -1
        total=start=0

        for i in range(len(gas)):
            total+= gas[i]-cost[i]

            if total <0:
                total=0
                start=i+1
        return start


        