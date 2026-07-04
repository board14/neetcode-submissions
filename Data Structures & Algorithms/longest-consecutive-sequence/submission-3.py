class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        nums.sort()
        n=len(nums)
        if not nums:
            return 0
        i=0
        cur,streak=nums[i],0
        while i<n:
            if i<n and cur!=nums[i]:
                streak=0
                cur=nums[i]
            while i<n and cur==nums[i]:
                i+=1
            streak+=1
            cur+=1
            res=max(streak, res)
        return res

        
        