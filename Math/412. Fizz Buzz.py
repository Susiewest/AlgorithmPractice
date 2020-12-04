刚好昨天的pytorch视频有提到这个:)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        def div(n):
            if n%15==0: return 3
            if n%5==0: return 2
            if n%3==0: return 1
            else: return 0
        for i in range(1,n+1):
            result.append([str(i), "Fizz", "Buzz", "FizzBuzz"][div(i)])
        return result

执行用时：52 ms, 在所有 Python3 提交中击败了76.62%的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了32.33%的用户
