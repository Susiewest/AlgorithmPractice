class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #可以先二分查找找到target的右边界 再找到左边界 然后right-left+1
        #如何找到右边界，就<=target的话，指针就往右找
        #可以定义一个找右边界的函数，找target和target-1的边界 然后相减即可
        target-1 代表着去查找比 target 小的首个数字的右边界, 并不一定真的找到/存在target-1
        def findMargin(target):
            left, right = 0, len(nums)-1
            while left<=right:
                mid = left+(right-left)//2 
                if nums[mid]<=target: left = mid+1
                else: right = mid-1
            return right
        return findMargin(target)-findMargin(target-1)
        
执行用时：32 ms, 在所有 Python3 提交中击败了96.02%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了18.24%的用户

