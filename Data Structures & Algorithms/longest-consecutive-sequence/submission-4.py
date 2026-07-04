class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        values=set(nums)

        for n in nums:
            if n-1 not in values:
                length=1
                while n+length in values:
                    length+=1
                res=max(length,res)
        return res

        