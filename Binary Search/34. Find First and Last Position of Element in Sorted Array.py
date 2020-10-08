#缺点：二分找到mid后 又线性查找的起点和终点 有待改进
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right=0, len(nums)-1
        result=[]
        while(left<=right):
            mid=left+(right-left)//2
            if nums[mid]==target:
                start, end=mid, mid
                while(start>=0 and nums[start]==target):
                    start-=1
                result.append(start+1)
                while(end<len(nums) and nums[end]==target):
                    end+=1
                result.append(end-1)
                return result
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [-1,-1]


'''执行用时：
40 ms, 在所有 Python3 提交中击败了79.35%的用户
内存消耗：
14.2 MB, 在所有 Python3 提交中击败了70.39%的用户'''
