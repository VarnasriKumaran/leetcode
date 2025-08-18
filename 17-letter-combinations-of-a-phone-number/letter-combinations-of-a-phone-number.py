class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number=dict()
        number[1]="#"
        a=97
        b=123

        number = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}


        # for i in range(2,10):
        #     if a<124:
        #         chars=[]
        #         if i==7 or i==9:
        #             for j in range(4):
        #                 chars.append(chr(a+j))
        #             a+=4
        #         for j in range(3):
        #             chars.append(chr(a+j))
        #         a+=3
        #         number[i]=''.join(chars)
        if not digits:
            return []
        result=[""]
        for num in digits:
            temp=[]
            for prefix in result:
                for i in number[num]:
                    temp.append(prefix+i)
            result=temp
        return result



        




            
        