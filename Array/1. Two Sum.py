首先这个题不能先排序再寻找，因为return的是元素下标，而非判断是否存在和为target的。
其次，要考虑寻找target-current存在，是不是current本身？每一个元素不能被使用两次，所以
一个办法是我们只需要在 x 后面的元素中寻找 target - x。
另一个方法是，将元素存入hashtable之前先判断target-x在不在，在，就return，不在，就放进去。这样就可以保证自己不会被用到两次。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            if target-nums[i] not in hash_table:
                hash_table[nums[i]] = i
            else:
                return [hash_table[target-nums[i]], i]
                

执行用时：36 ms, 在所有 Python3 提交中击败了84.53%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了58.12%的用户
