class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt_zero=0
        product=1
        res=[0]*n
        for i in range(n):
            if nums[i]==0:
                cnt_zero+=1
            else:
                product*=nums[i]
        if cnt_zero>=2:
                return res
                
        if cnt_zero==1:
            for i in range(n):
                if nums[i]==0:
                    res[i]=product
                else:
                    res[i]=0
                    
            return res
        else:
            for i in range(n):
                res[i]=int(product/nums[i])
            return res



        