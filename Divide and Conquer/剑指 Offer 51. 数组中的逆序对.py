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

写了没有[]参数的版本，感觉也没事，tmp并不是递归更新的，而是一开始就放了个完整长度的，不断重填，另开一个空list也行
划分的时候不做任何操作，合并的时候，可以在第一个list中元素加入结果时计数（1），也可以按照第二个list中元素加入结果时计数（2）
[left, mid] 有序 [mid+1,right]有序
（1）只需在第一个元素出列时，数一数后面数组已经出列了几个元素 j-mid-1
（2） 只需要第二个数组中的元素出列时，数一数前面数组还剩多少个数字 mid-i+1
注意 当nums[i]==nums[j]时也要计数
+= 不要写成 =
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort(nums, left, right):
            if left>=right:
                return 0
            mid = (left + right)//2
            inverse_count = mergesort(nums, left, mid)+mergesort(nums, mid+1, right)
            i, j = left, mid+1
            cur = []
            while i<=mid and j<=right:
                # =也要计数
                if nums[i]<=nums[j]:
                    cur.append(nums[i])
                    i += 1
                    inverse_count += j-mid-1
                else:
                    cur.append(nums[j])
                    j += 1                   
            while i<=mid:
                cur.append(nums[i])
                inverse_count += j-mid-1
                i += 1
            while j<=right:
                cur.append(nums[j])
                j += 1
            nums[left:right+1] = cur
            return inverse_count
        return mergesort(nums, 0, len(nums)-1)
                
执行用时：964 ms, 在所有 Python3 提交中击败了95.84%的用户
内存消耗：20.1 MB, 在所有 Python3 提交中击败了62.77%的用户

