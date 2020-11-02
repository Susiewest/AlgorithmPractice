class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # hashchart=[i for i in range(len(nums)+1)]
        # for i in range(len(nums)):
        #     if nums[i] in hashchart:
        #         hashchart.remove(nums[i])
        # return hashchart[0]
        #2.
        # hashset=set(nums)
        # for i in range(len(nums)+1):
        #     if i not in hashset:
        #         return i
        #执行用时：40 ms, 在所有 Python3 提交中击败了95.87%的用户
        #内存消耗：15 MB, 在所有 Python3 提交中击败了5.90%的用户
        #3. 
        result=len(nums) 
        for i in range(len(nums)):
            result^=nums[i]^i
        return result
执行用时：44 ms, 在所有 Python3 提交中击败了89.67%的用户
内存消耗：14.6 MB, 在所有 Python3 提交中击败了14.88%的用户
