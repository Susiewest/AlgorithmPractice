class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        front, end=0, len(nums)-1
        current=0
        while(current<=end):
            if nums[current]==0:
                nums[front],nums[current]=nums[current],nums[front]
                #swap(nums[front],nums[current])
                front+=1
                current+=1
            elif nums[current]==2:
                nums[current],nums[end]=nums[end],nums[current]
                #swap(nums[current],nums[end])
                end-=1
                #一开始报错了！！！后来把下面这句注释掉就ok了！因为和前面的对换不会有2换到当前位置，只可能是1
                #但是和后面换 可能换来了2！当前的current还需要再执行一次操作！
                #current+=1
            else:
                current+=1
'''执行用时：
40 ms, 在所有 Python3 提交中击败了71.71%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了5.82%的用户'''
