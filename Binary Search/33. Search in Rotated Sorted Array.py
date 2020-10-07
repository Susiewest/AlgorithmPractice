class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        while(left<=right):
            #一个疑惑 原本我的二分是写的left+（right-left+1）//2 
            #偶数个的时候每次取右边那个做mid 就会报错 【3，1】 3 return了-1
            #而不是return 0
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<nums[right]: #右半边有序
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1 #找[mid,right]
                else:
                    right=mid-1
            else:    #左半边有序
                if nums[0]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return -1


'''执行用时：
40 ms, 在所有 Python3 提交中击败了74.87%的用户
内存消耗：
13.3 MB, 在所有 Python3 提交中击败了91.67%的用户'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right=0, len(nums)-1
        while(left<=right):
            #这个版本保留了原本的取mid写法
            #在39行进行了改动 原本是if mid<right改成了mid<=right 之前的写法取中间两个数中右边的数 如果右边的数就是最右端的数 会跳到else执行 判定为mid和左半边有序
            mid=left+(right-left+1)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[right]: #右半边有序
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1 #找[mid,right]
                else:
                    right=mid-1
            else:    #左半边有序
                if nums[0]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return -1
        
'''执行用时：
36 ms, 在所有 Python3 提交中击败了90.81%的用户
内存消耗：
13.5 MB, 在所有 Python3 提交中击败了31.63%的用户'''

