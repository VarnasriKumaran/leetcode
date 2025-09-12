# Last updated: 9/12/2025, 11:17:08 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins=[amount+1]*(amount+1)
        min_coins[0]=0

        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    min_coins[i]=min(min_coins[i],1+min_coins[i-c])
        return min_coins[-1] if min_coins[-1]!=amount+1 else -1
    # count=0
    # def func_coin(curr):
    #         x=nums[0]
    #         bal=curr-x
    #         if bal in coins:
    #             count+=1
    #             return count+1
    #         else:
    #             return func_coin(bal)
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     out=0
    #     min_coins_req=float('inf')
    #     coins_req=self.func_coin(amount)
    #     min_coins_req=min(coins_req,min_coins_req)


        


        