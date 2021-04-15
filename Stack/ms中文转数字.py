class Solution:
    def trans(self,chinese_num):
        stack = []
        chart = {'零':0,'一':1, '二':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10, '百':100, '千':1000, '万':10000}
        chinese_num = list(chinese_num)
        result = 0
        for cn_char in chinese_num:
            temp_num = chart[cn_char]
            if not stack or temp_num<stack[-1]:
                stack.append(temp_num)
            else:
                temp = 0
                while stack and stack[-1]<temp_num:
                    temp += stack.pop()
                stack.append(temp*temp_num)
        return sum(stack)

sol = Solution()
ans = sol.trans('三十万二千五百二十三')
print(ans)

