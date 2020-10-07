#一个大总结！为了避免死循环，把区间分成两个部分的时候，二分最后一次的中间数划分很重要。
#如果选定左端和mid比 此时mid取右中位数写起来比较方便 选定右端和mid比 此时mid取左中位数比较方便！
#当然也可以写左端和mid左中位数 右端和右中位数 我的方法1是右端和左中位数 方法2是右端和右中位数
#https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/er-fen-fa-python-dai-ma-java-dai-ma-by-liweiwei141/
#链接的评论区有四种写法的合集 可以看看
#当处理完简单的部分（有序的一部分）后，剩余的复杂的部分可能迎刃而解。本问题，只需要将眼光聚焦于有序的部分，就会简单很多。
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
            #在45行进行了改动 原本是if mid<right改成了mid<=right 之前的写法取中间两个数中右边的数 如果右边的数就是最右端的数 会跳到else执行 判定为mid和左半边有序
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

