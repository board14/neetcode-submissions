class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        
        for i in range(len(nums)):
            prod=1
            j=0
            while(j<len(nums)):
                if j==i:
                    j+=1
                    continue
                else:
                    prod*=nums[j]
                j+=1
            res[i]=prod
        
        return res


        