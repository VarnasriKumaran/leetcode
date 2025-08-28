class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        if nums is None:
            return []
        
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1

            
            while(j<k):
                total=nums[i]+nums[j]+nums[k]

                if total>0:
                    k-=1
                elif total<0:
                    j+=1
                elif total==0:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return ans
                    




        # nums.sort()
        # while(j<k):
        #     if nums[i]+nums[j]+nums[k]==0:
        #         ans.append([nums[i],nums[j],nums[k]])
        #         i=i+1
        #         j=j+1
        #         k=k-1
        #     if nums[i]+nums[j]+nums[k]<0:
        #         i+=1
        #         j+=1
        #     if nums[i]+nums[j]+nums[k]>0:
        #         k-=1
        # dis=set()
        # res=[]
        # for i in ans:
        #     i=tuple(sorted(i))
        #     if i not in dis:
        #         dis.add(i)
        #         res.append(i)
        # return ans


        # # # ans=[]

        # # # for i in range(len(nums)):
        # # #     for j in range(i+1,len(nums)):
        # # #         for k in range(j+1,len(nums)):
        # # #             if nums[i]+nums[j]+nums[k]==0:
        # # #                 ans.append([nums[i],nums[j],nums[k]])
        # # # dis=set()
        # # # res=[]
        # # # for i in ans:
        # # #     i=tuple(sorted(i))
        # # #     if i not in dis:
        # # #         dis.add(i)
        # # #         res.append(i)


        # # # return res