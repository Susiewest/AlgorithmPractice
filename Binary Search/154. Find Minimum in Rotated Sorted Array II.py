class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            elif nums[mid]<nums[right]:
                right = mid
            else:
                return min(nums)
        return nums[left]

执行用时：36 ms, 在所有 Python3 提交中击败了69.85%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了95.67%的用户

