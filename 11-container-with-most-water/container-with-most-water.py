class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        w=0
        cap=0
        water=0

        while(l<r):
            w=r-l
            if height[l]<height[r]:
                cap=height[l]
                l+=1
            else:
                cap=height[r]
                r-=1
            water=max(water, w*cap)
        return water

        