class Solution:
    def reverseBits(self, n: int) -> int:

        temp=bin(n)[2:].zfill(32)
        reverse_temp= temp[::-1]
        return int(reverse_temp,2)          
        