哈希 时间o(n) 空间o(n)
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        counter={}
        for i in range(len(nums)):
            if nums[i] in counter:
                return nums[i]
            else:
                counter[nums[i]]=1

执行用时：44 ms, 在所有 Python3 提交中击败了95.81%的用户
内存消耗：22.6 MB, 在所有 Python3 提交中击败了32.85%的用户

空间o（1）
长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内，那么排好序的时候，数字nums[i]就应该在下标i的位置上
所以 如果nums[i]和i不等，就把nums[i]换到第nums[i]位置上，即nums[nums[i]]和num[i]互换（此时如果nums[nums[i]]数字是对的，那就重复了直接return，不对才换
换完还不能继续处理下一个数，要看当前nums[i]数字对了没，没对继续处理，直到对了/换的时候发现别人已经对了
有个很高级的名字 叫鸽巢原理 也叫抽屉原理 “如果每个抽屉代表一个集合，每一个苹果就可以代表一个元素，假如有n+1个元素放到n个集合中去，其中必定有一个集合里至少有两个元素。” 
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while(nums[i]!=i):
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                elif nums[i]!=nums[nums[i]]:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                    #************nums[i]，nums[nums[i]] = nums[nums[i]]，nums[i] 这样写就超时了 是错的 为什么啊啊啊啊啊啊啊***********
                    #可以用一个数组试一下，例如nums=[1,2,3,4,5], 
                    #nums[0], nums[nums[0]] = nums[nums[0]], nums[0]
                    #交换后原数组a变为[2,2,1,4,5]，简单的说原因就是nums[i]的值发生了变化，nums[nums[i]]指向了不同的位置。
                    #nums[0]=1, nums[0]=nums[nums[0]]=2, nums[nums[0]]=nums[2]=nums[0]=2

执行用时：52 ms, 在所有 Python3 提交中击败了78.60%的用户
内存消耗：22.5 MB, 在所有 Python3 提交中击败了85.38%的用户
