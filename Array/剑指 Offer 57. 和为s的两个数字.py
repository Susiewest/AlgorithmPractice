双指针
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while(left<right):
            if nums[left]+nums[right]==target:
                return [nums[left],nums[right]]
            elif nums[left]+nums[right]<target:
                left+=1
            else:
                right-=1
        return []
执行用时：124 ms, 在所有 Python3 提交中击败了86.55%的用户
内存消耗：25.4 MB, 在所有 Python3 提交中击败了31.31%的用户

