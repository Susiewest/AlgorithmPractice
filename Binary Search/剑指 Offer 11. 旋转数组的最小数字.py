感觉发现了书里的一个bug，p86，这里找二分做比较的时候只能和right比较大小，因为right是确定在右排序列表里面的，而left不一定在左排序列表里
如[1,3,5] mid比left大，按理说在左边，然后去右边找最小值，就找错了，此时left到right都属于右排序列表，整个list里没有左排序列表。
而right一定在右排序列表。所以和nums[right]比
当num[mid] = nums[right]的时候，最小值不知道在哪边，[0,1,1,1,1],[1,1,1,0,1]都有可能，直接用O(n)的办法解决了。
class Solution:
    def minArray(self, numbers: [int]) -> int:
        left, right = 0 ,len(numbers)-1
        while(left<right):
            mid = (left+right)//2
            if numbers[mid]>numbers[right]:
                left = mid+1
            elif numbers[mid]<numbers[right]:
                right = mid
            else:
                return min(numbers)
        return numbers[left]
执行用时：36 ms, 在所有 Python3 提交中击败了88.39%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了44.86%的用户
