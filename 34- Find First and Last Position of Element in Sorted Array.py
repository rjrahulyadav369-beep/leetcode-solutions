class Solution(object):
    def lowerbound(self,nums,target):
        n=len(nums)
        lb=-1
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb        
    def upperbound(self,nums,target):
        n=len(nums)
        ub=n
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1  
        return ub                          
    def searchRange(self, nums, target):
        lbb=self.lowerbound(nums,target)
        if lbb==-1 or nums[lbb]!=target:
            return[-1,-1]
        ubb=self.upperbound(nums,target)
        return [lbb,ubb-1]    
      
