class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        p=(n)*(n+1)/2
        sum=0
        for i in nums:
            sum=sum+i
        return p-sum    

         
        
