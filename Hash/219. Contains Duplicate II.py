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
