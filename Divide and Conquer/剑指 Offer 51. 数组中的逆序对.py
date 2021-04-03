暴力超时 分治 归并——划分的时候不做任何操作，合并的时候才计算inverse_count
疑问：如果不把tmp作为参数传入会怎样？
class Solution:
    def mergeSort(self, nums, tmp,left, right):
        if left>=right:
            return 0
        mid = (left+right)//2
        inverse_count = self.mergeSort(nums, tmp, left, mid)+self.mergeSort(nums, tmp, mid+1, right)
        i, j, pos = left, mid+1, left
        while i<=mid and j<=right:
            if nums[i]<=nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inverse_count += j-(mid+1)
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid+1):
            tmp[pos] = nums[k]
            inverse_count += j-(mid+1)
            pos += 1
        for k in range(j, right+1):
            tmp[pos] = nums[k]
            pos += 1
        nums[left:right+1] = tmp[left:right+1]
        return inverse_count

        
    def reversePairs(self, nums: List[int]) -> int:
        tmp = [0]*len(nums)
        
        return self.mergeSort(nums,tmp, 0,len(nums)-1)
      
执行用时：1320 ms, 在所有 Python3 提交中击败了83.40%的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了96.12%的用户

