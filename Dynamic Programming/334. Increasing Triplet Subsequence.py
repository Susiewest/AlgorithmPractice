subsequence不要求得到的子序列是连续的？

题目要求O(N)的时间复杂度 O(1)的空间复杂度
以下写法为o（n2）的时间复杂度 o（n）的空间复杂度（。。
那么为什么要这么写呢 因为我担心我连on2都写不出来 动态规划一生之敌 还好写出来了。。。
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)>=3

执行用时：4412 ms, 在所有 Python3 提交中击败了7.68%的用户
内存消耗：14.2 MB, 在所有 Python3 提交中击败了27.45%的用户

额 一个很小的优化 就是不等所有dp算完再return 每次更新dp的时候就判断+return
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums:
            return False
        dp = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
                    if dp[i]>=3:
                        return True

执行用时：3808 ms, 在所有 Python3 提交中击败了10.86%的用户
内存消耗：14.3 MB, 在所有 Python3 提交中击败了10.82%的用户

first, second 分别记录第一小和第二小的数
遇到比first小的替换first，遇到比first大比second小的替换second
遇到比second大的，ok fine return true
一些反例的思考： [5，6，1，7]应该return true 遇到1更新first，但不会影响second，second存在就意味着前面有比second小的数，自己前面存在着一个比自己小的元素，
最后first：1 second：6 尽管不是我们想找到的567，但不会影响true/false的判断
结论：
遇到更小的first，不会影响second，也不会影响寻找一个比second大的数
遇到更小的second，既然走到这里还没停下，就意味着没有比更新前的second更大的数，所以替换成一个更小的 新的second，也不会影响后面找大的数，反而降低了找大的数的标准～
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float(inf), float(inf)
        for i in range(len(nums)):
            if nums[i]<first:
                first = nums[i]
            elif first<nums[i]<second:
                second = nums[i]
            elif nums[i]>second:
                return True
        return False            

执行用时：64 ms, 在所有 Python3 提交中击败了89.80%的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了33.94%的用户

