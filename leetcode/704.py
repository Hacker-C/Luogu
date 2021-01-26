class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        flag=1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
                flag=0
                break
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        if flag:
            return -1
