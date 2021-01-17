双指针 滑动窗口
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        left, right = 1, 1
        window_sum = 1
        result = []
        while left<=target//2:
            if window_sum<target:
                right += 1
                window_sum += right
            elif window_sum>target:
                window_sum -= left
                left += 1                
            else:
                result.append([i for i in range(left,right+1)])
                window_sum -= left
                left += 1
        return result
执行用时：104 ms, 在所有 Python3 提交中击败了80.50%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了20.83%的用户

