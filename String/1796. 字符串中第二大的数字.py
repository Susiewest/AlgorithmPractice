class Solution:
    def secondHighest(self, s: str) -> int:
        digit_pattern = r'[0-9]'
        digit = re.findall(digit_pattern, s)
        digit = list(set(digit))
        digit.sort()
        try:
            return int(digit[-2]) 
        except:
            return -1

执行用时：32 ms, 在所有 Python3 提交中击败了99.27%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了81.24%的用户


