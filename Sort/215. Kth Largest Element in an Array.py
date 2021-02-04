import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = [nums[i] for i in range(k)]
        heapq.heapify(hp)
        for i in range(k,len(nums)):
            if nums[i]>hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp,nums[i])
        return hp[0]

执行用时：44 ms, 在所有 Python3 提交中击败了78.80%的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了31.16%的用户

