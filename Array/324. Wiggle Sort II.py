#测试用例41/44
#学到了切片插入，nums[1,2,3,4,5] nums[0::2]=[1,3,5] nums[1::2]=[2,4]
#nums排序，然后让135的位置等于大的后半部分，246等于小的前半部分
#但无法保证绝对大于 只能保证大于等于，如[4,5,5,6]处理后还是[4,5,5,6]，正确的排法应该是[5,6,4,5]
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        slot = (len(nums)+1)//2
        #学到了切片插入，nums[1,2,3,4,5] nums[0::2]=[1,3,5] nums[1::2]=[2,4]
        #nums排序，然后让135的位置等于大的后半部分，246等于小的前半部分
        nums[0::2], nums[1::2] = nums[:slot], nums[slot:]
        return nums
        
显然，出现上述现象是因为nums中存在重复元素。实际上，由于穿插之后，相邻元素必来自不同子数组，所以A或B内部出现重复元素是不会出现上述现象的。所以，出现上述情况其实是因为数组A和数组B出现了相同元素，我们用r来表示这一元素。而且我们可以很容易发现，如果A和B都存在r，那么r一定是A的最大值，B的最小值，这意味着r一定出现在A的尾部，B的头部。其实，如果这一数字的个数较少，不会出现这一现象，只有当这一数字个数达到原数组元素总数的一半，才会在穿插后的出现在相邻位置。以下举几个例子进行形象地说明：

例如，对于数组[1,1,2,2,3,3],分割为[1,1,2]和[2,3,3]，虽然A和B都出现了2，但穿插后为[1,2,1,3,2,3]，满足要求。
而如果2的个数再多一些，即[1,1,2,2,2,3]，分割为[1,1,2]和[2,2,3]，最终结果为[1,2,1,2,2,3]，来自A的2和来自B的2出现在了相邻位置。

出现这一问题是因为重复数在A和B中的位置决定的，因为r在A尾部，B头部，所以如果r个数太多（大于等于(length(nums) + 1)/2），就可能在穿插后相邻。要解决这一问题，我们需要使A的r和B的r在穿插后尽可能分开。一种可行的办法是将A和B反序：

例如，对于数组[1,1,2,2,2,3]，分割为[1,1,2]和[2,2,3]，分别反序后得到[2, 1, 1]和[3, 2, 2]，此时2在A头部，B尾部，穿插后就不会发生相邻了。

当然，这只能解决r的个数等于(length(nums) + 1)/2的情况，如果r的个数大于(length(nums) + 1)/2，还是会出现相邻。但实际上，这种情况是不存在有效解的，也就是说，这种数组对于本题来说是非法的。

作者：hexcat
链接：https://leetcode-cn.com/problems/wiggle-sort-ii/solution/yi-bu-yi-bu-jiang-shi-jian-fu-za-du-cong-onlognjia/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

逆序解决重复元素问题
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        slot = len(nums)//2
        #学到了切片插入，nums[1,2,3,4,5] nums[0::2]=[1,3,5] nums[1::2]=[2,4]
        #nums排序，然后让135的位置等于大的后半部分，246等于小的前半部分
        nums[1::2],nums[0::2] = nums[:slot], nums[slot:]
        return nums
        
执行用时：44 ms, 在所有 Python3 提交中击败了94.87%的用户
内存消耗：14.4 MB, 在所有 Python3 提交中击败了57.98%的用户
