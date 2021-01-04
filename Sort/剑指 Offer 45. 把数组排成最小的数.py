跟179题差不多 一个要最大数 一个要最小数
都要考虑拼接后的影响，比如3和30，如果直接从小到大排序再拼接，得到的会是330，但其实我们想要303

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def fastsort(left, right):
            if left>=right:
                return
            i, j = left, right
            #选left做pivot？
            pivot = str_num[left]
            while i<j:
                while i<j and pivot+str_num[j]<=str_num[j]+pivot:
                    j-=1
                str_num[i]=str_num[j]
                while i<j and pivot+str_num[i]>=str_num[i]+pivot:
                    i+=1
                str_num[j]=str_num[i]
            str_num[i] = pivot
            fastsort(left,i-1)
            fastsort(i+1,right)
        str_num = [str(num) for num in nums]
        fastsort(0,len(nums)-1)
        return ''.join(str_num)
        
执行用时：44 ms, 在所有 Python3 提交中击败了75.29%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.16%的用户

