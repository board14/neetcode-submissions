class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        result=0
        for i  in range(n):
            for j in range(i+1,n):
                # j=i+1
                w=j-i
                l=min(heights[i],heights[j])
                area=w*l
                result=max(area,result)
        return result

        