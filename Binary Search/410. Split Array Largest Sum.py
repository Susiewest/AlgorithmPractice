class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x):
            count, total =1, 0
            for num in nums:
                if total+num>x:
                    total = num
                    count += 1
                else:
                    total += num
            return count <= m
        left, right = max(nums), sum(nums)
        while left<right:
            mid = (left+right)//2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

执行用时：44 ms, 在所有 Python3 提交中击败了61.27%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了28.92%的用户


