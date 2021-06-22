将左边的一个较小元素和右边的一个较大元素互换，较小元素要尽可能的靠右，较大元素尽可能的小
交换完成后，较大元素右边要调整顺序，调为最小，即数字按升序排列
这样可以保证新排列在大于原排列的情况下，变大幅度尽可能小
经过分析，交换后，较大元素右侧为降序排列，直接双指针反转即可

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        less = len(nums)-2
        # 从右往左找到第一个小于右侧元素的的 如4，7，6，5，3 找到4
        # less>=0 不写会越界，而且也无法正确执行less<0的情况（nums直接是最大）
        while less>=0 and nums[less]>=nums[less+1]:  #**
            less -= 1
        # 若整个nums都是降序，那么已经是最大的排列了，直接反转变成最小的排列，跳过if里面的部分直接双指针反转
        if less>=0:                                 #**
            # 找到第一个比nums[less]大的
            more = len(nums)-1
            # 这里的=也很关键啊啊啊，一定要找比nums[less]大的，而非小或者一样大的
            while nums[more]<=nums[less]:           #**
                more -= 1
            nums[less], nums[more] = nums[more], nums[less]
            # 把less+1：的元素统统反转（即less+1到最后一个元素 都是降序的，全变成升序）
        left, right = less+1, len(nums)-1
        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
        
        
执行用时：44 ms, 在所有 Python3 提交中击败了42.03%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了46.52%的用户

