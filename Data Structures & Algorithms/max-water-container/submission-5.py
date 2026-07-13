class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        result=0
        l,r=0,n-1
        while l<r:
            w=r-l
            le=min(heights[l],heights[r])
            area=w*le
            result=max(area,result)
            if heights[l]>=heights[r]:r-=1
            else: l+=1
            
            
        
        return result

        