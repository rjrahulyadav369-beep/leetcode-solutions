class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        lb=0
        low=0
        high=n-1
        if nums[0]>=target:
            return 0
        elif nums[n-1]<target:
            return n    
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb            
                

       
