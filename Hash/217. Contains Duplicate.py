class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter=collections.Counter(nums)
        for i in range(len(nums)):
            if counter[nums[i]]>1:
                return True
        return False


'''执行用时：
52 ms, 在所有 Python3 提交中击败了49.39%的用户
内存消耗：
20.6 MB, 在所有 Python3 提交中击败了5.20%的用户'''
