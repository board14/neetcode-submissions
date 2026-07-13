class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        n=len(height)

        for i in range(n):
            lmax=rmax=height[i]
            for j in range (0,i):
                lmax=max(height[j],lmax)
            for j in range(i+1,n):
                rmax=max(height[j],rmax)
            
            result+=min(lmax,rmax)-height[i]
            print(result)
        return result
        