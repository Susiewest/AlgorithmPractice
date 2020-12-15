憨憨敬礼式做法
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        nums = odd+even
        return nums
执行用时：44 ms, 在所有 Python3 提交中击败了98.39%的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了5.16%的用户

可以用双端队列，偶数走后门，奇数走前门
也可以用快排的方法，双指针，遇到不符合要求的就和另一个指针换，然后另一个指针再走，下面试一下这个方法
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        while left<right:
            while left<right and nums[left]%2==1:
                left+=1
            nums[right], nums[left] = nums[left], nums[right]
            while left<right and nums[right]%2==0:
                right-=1
            nums[left], nums[right] = nums[right], nums[left]
        return nums
执行用时：52 ms, 在所有 Python3 提交中击败了87.94%的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了5.16%的用户

