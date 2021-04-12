1. 字符串可以直接降序排列，但是相同数字开头的会出现问题，比如‘30’会排在‘3’前面，而‘303‘不是我们想要的，我们想要‘330‘
此外 我先定义了gt 而非lt 303和330的情况依然会出现
2. 使用map函数 list的数据结构也发生了变化，sort是列表方法,只能对列表排序，要想对map排序可以用sorted
3. sorted返回的是副本，而非数组本身排序 所以要把sorted的结果赋值给一个变量
4. sort的底层是归并 也许只是用lt不使用gt 令reverse=true代表从大到小排，不知道底层是使用了gt呢 还是lt后倒序？如果定义gt 其他的都会排好序，除了最后拼成303而非330 很奇怪
class StrGt(str):
    def __lt__(x, y):
        return x+y<y+x
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #map() 会根据提供的函数对指定序列做映射。
        #第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
        #str_nums = map(str, nums)
        str_nums = [str(nums[i]) for i in range(len(nums))]
        str_nums.sort(key=StrGt, reverse=True)
        result = ''.join(str_nums)
        return '0' if result[0]=='0' else result

执行用时：44 ms, 在所有 Python3 提交中击败了80.62%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了7.16%的用户

参考剑指45的做法

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #map() 会根据提供的函数对指定序列做映射。
        #第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
        #str_nums = map(str, nums)
        def fastsort(left, right):
            if left>=right:
                return 
            pivot = str_nums[left]
            i, j = left, right
            while i<j:
                while i<j and str_nums[j]+pivot>=pivot+str_nums[j]:
                    j -= 1
                str_nums[i] = str_nums[j]
                while i<j and str_nums[i]+pivot<=pivot+str_nums[i]:
                    i += 1
                str_nums[j] = str_nums[i]
            str_nums[i] = pivot
            fastsort(left, i-1)
            fastsort(i+1, right)
        str_nums = [str(i) for i in nums]
        fastsort(0, len(nums)-1)
        str_nums = str_nums[::-1]
        result = ''.join(str_nums) 
        return result if int(result) else '0'

执行用时: 44 ms
内存消耗: 15.1 MB

