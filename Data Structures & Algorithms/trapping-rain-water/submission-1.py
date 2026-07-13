class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        n=len(height)

        larr=[0]*n
        rarr=[0]*n
        larr[0]=lmax=height[0]
        rarr[n-1]=rmax=height[n-1]
        for i in range(1,n):    
            larr[i]=lmax=max(height[i],lmax)
        for i in range(n-2,-1,-1):    
            rarr[i]=rmax=max(height[i], rmax)
        for i in range(n):
            result+=min(larr[i],rarr[i])-height[i]
        return result

            
        