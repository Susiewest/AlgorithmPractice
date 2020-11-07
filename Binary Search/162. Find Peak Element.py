https://www.cnblogs.com/kyoner/p/11080078.html 不错的博客
但此题在套路之外 很有意义的二分 yes！
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1 #搜索范围是[0,len-1] 闭区间
        while(left<right): #终止条件是left==right [left, right]=[left,left]还能取一个数字
            #此时它必定就是了，如果继续执行 left right一直等于mid 永远也不会结束
            #闭区间上查,按理说是要用<=的，但如果继续执行有可能right一直不变，死循环超时，所以用<号,最后退出循环时[l,l]或者[r,r]是不会查的
            mid = (right+left)//2
            if nums[mid]<nums[mid+1]: #mid不可能是了 下一个区间从[mid+1,right]
                left=mid+1
            else:   #mid可能是 下一个区间从[left,mid]
                right=mid
        return left #终止条件是left==right 那么最终return left/right 都一样了

sol=Solution()
ans=sol.findPeakElement([1,2,3,1])
print(ans)

        
执行用时：40 ms, 在所有 Python3 提交中击败了70.70%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.87%的用户
