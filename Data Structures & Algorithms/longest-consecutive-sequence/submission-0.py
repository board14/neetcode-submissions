class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        stre=set(nums)

        for num in nums:
            streak,cur=0,num
            while cur in stre:
                cur+=1
                streak+=1
            res=max(streak,res)
        return res