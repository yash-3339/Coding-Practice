#https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count=len(nums)
        valid=len(set(nums))
        if (count>valid):
            return True
        else:
            return False    
        # x=[]
        # for i in nums:
        #     if i in x:
        #         return True
        #     else:
        #         x.append(i)   
        # return False