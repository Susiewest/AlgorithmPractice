前缀和+hash
hash保存当前位置之前所有前缀和的 {大小：个数}
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
      # 为什么一定要0开头，因为要包含前缀和=goal的情况，如果不是0开头，那将不计数从第一个位置开始的list
        prefix = [0]+list(accumulate(nums))
        count = 0
        hash_dict = {}
        for i in range(len(nums)+1):
            if prefix[i]-goal in hash_dict.keys():
                count += hash_dict[prefix[i]-goal]
            if prefix[i] in hash_dict.keys():
                hash_dict[prefix[i]] += 1
            else:
                hash_dict[prefix[i]] = 1               

        return count
执行用时：280 ms, 在所有 Python3 提交中击败了31.62%的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了20.38%的用户
