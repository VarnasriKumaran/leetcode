class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        i=0
        while j < len(s) and i < len(t):
            if s[j]==t[i]:
                j+=1
            i+=1
        if j==len(s):
            return True
        return False

        