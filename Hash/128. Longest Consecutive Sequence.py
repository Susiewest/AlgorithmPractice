对每一个新数字，找他-1和他+1在dict里保存的长度。
为什么只更新两端的值？
因为只有两端的值可能会继续延伸，所以要保存最新的长度，再有中间的值对最大长度是没有影响的，所以只需要更新头和尾的值
也就是hash_dict(num)存啥其实无所谓，只需要知道num在dict里即可（但我没写 hash_dict[num] = 也没有报错
这是因为如果num前不着村/后不着店（num-1，num+1都不在dict里），那么num-left==num/num+right==num，也占位了。其他情况（左&右有延伸）不需要占位。

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict = dict()
        nums = set(nums)
        max_length = 0
        for num in nums:
            if num not in hash_dict.keys():
                left = hash_dict.get(num-1, 0)
                right = hash_dict.get(num+1, 0)
                current_length = left+right+1
                max_length = max(max_length, current_length)
                # hash_dict[num] = current_length
                hash_dict[num-left] = current_length
                hash_dict[num+right] = current_length
        return max_length
       
       
执行用时：80 ms, 在所有 Python3 提交中击败了51.85%的用户
内存消耗：38.2 MB, 在所有 Python3 提交中击败了5.01%的用户

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0
        for num in nums:
            # 很关键的一点，如果num-1在set里，那num一定被遍历过计数过了，没必要重新遍历
            if num-1 not in nums:
                current_length = 1
                while num+1 in nums:
                    num = num+1
                    current_length += 1
                max_length = max(max_length, current_length)
        return max_length
    
执行用时：68 ms, 在所有 Python3 提交中击败了68.57%的用户
内存消耗：25.9 MB, 在所有 Python3 提交中击败了71.86%的用户
