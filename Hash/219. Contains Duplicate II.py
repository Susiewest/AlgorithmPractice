#遇到一些问题改了好一会 结果最后一个测试用例超时了 怒了 拳头紧握 睡醒再做
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = False
        #for i in range(len(nums) - k):不行呀 测试用例根本不用保证不越界
        for i in range(len(nums)):
            # temp_counter={}
            #temp_num=nums[i:i+k+1]
            if i+k+1<len(nums):
                temp_counter = collections.Counter(nums[i:i+k+1]) 
            else:
                temp_counter = collections.Counter(nums[i:])  
            for j in range(len(nums)):
                #Counter计数器似乎只能根据键值调用 不能根据下标调用 
                #我一开始写的temp_counter[j]>1| for j in range(len(temp_counter)) 
                #不行 调用不对
                if temp_counter[nums[j]] > 1:
                    result = True
        return result

    
#之前是滑动窗口 每k个数字生成一个counter 超时了
#现在是从头到尾走一遍即可 遇到已存在于字典的数字就判断下标距离
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter={}
        for i in range(len(nums)):
            if nums[i] in counter.keys() and counter[nums[i]]>=i-k:
                return True
            counter[nums[i]]=i
        return False
'''执行用时：
44 ms, 在所有 Python3 提交中击败了89.26%的用户
内存消耗：
21.3 MB, 在所有 Python3 提交中击败了54.35%的用户'''
