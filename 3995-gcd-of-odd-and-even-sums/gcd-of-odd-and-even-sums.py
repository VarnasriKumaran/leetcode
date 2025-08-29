class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        max_len=n*2
        even_sum=0
        odd_sum=0

        for i in range(1,max_len):
            if i%2==0:
                even_sum+=i
            else:
                odd_sum+=i

        while(odd_sum!=0):
            even_sum,odd_sum=odd_sum,even_sum%odd_sum
        return even_sum
        