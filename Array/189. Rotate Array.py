class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,start,end):
            while(start<end):
                temp=nums[start]
                nums[start]=nums[end]
                nums[end]=temp
                start+=1
                end-=1
                #wow看答案才知道原来python可以直接
                #nums[start],nums[end]=nums[end],nums[start]
                #不用担心被覆盖掉
        n=len(nums)
        #第一次写的版本无下面这行 会导致k>len的时候没法做
        k=k%n
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)


'''执行用时：
44 ms, 在所有 Python3 提交中击败了67.11%的用户
内存消耗：
14 MB, 在所有 Python3 提交中击败了5.20%的用户'''
