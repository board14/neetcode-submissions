class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs={}
        a=[]
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in hs:
                return[hs[diff],i]
            else:
                hs[nums[i]]=i

        
        