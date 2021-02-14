haha 每次觉得自己对二分法更深一点理解以后就会飞快忘掉自己的感悟
这个题和162题有点类似，就是明明是探索闭区间，但是最后剩一个数不会去判断，不然就会死循环
然后就是如果最后区间剩下两个数，比如[left,left+1]，如果取左中位数依然会死循环，因为写了left=mid，每次mid都是left本身，然后一直执行left=mid，区间不缩小
好像162题只需要写不判断[left,left]就可以解决死循环，这个题不行，这个题最好是计算mid算右中位数才能破防
使用二分查找法搜索，注意特值对搜索边界的影响。区间如果不发生收缩 就会死循环！！！

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x//2+1 #x=1时解为1，x//2+1保证了可以找到1
        while left<right:
            mid = (left+right+1)//2
            if mid*mid>x:
                right = mid-1
            else:
                left = mid
        return left
执行用时：52 ms, 在所有 Python3 提交中击败了42.43%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了6.09%的用户

