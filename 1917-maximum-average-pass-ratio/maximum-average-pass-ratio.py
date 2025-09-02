class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ans=[]
        sum_arr=0.0
        for p,q in classes:
            sum_arr+=p/q
            r=((p-q)/(q*(q+1)))
            ans.append((r,p,q))
        heapify(ans)

        while extraStudents>0:
            r1,p,q=ans[0]
            if r1==0:
                break
            sum_arr-=r1
            r2=((p-q)/((q+2.0)*(q+1.0)))
            extraStudents-=1
            heapreplace(ans,(r2,p+1,q+1))
        return sum_arr/len(classes)
        



        