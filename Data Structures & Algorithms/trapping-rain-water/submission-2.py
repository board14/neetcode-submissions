class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        n=len(height)
        l,r=0,n-1
        lmax,rmax=height[0], height[n-1]
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(height[l],lmax)
                result+=lmax-height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                result+=rmax-height[r]
        return result



            
        