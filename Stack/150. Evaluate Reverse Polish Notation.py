import collections
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= collections.deque()
        operations={'+','-','*','/'}
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                stack.append(tokens[i])
            else:
                temp1 = stack.pop()
                temp2 = stack.pop()
                if tokens[i]=='+':
                    stack.append(int(temp1)+int(temp2))
                elif tokens[i]=='-':
                    stack.append(int(temp2)-int(temp1))
                elif tokens[i]=='*':
                    stack.append(int(temp1)*int(temp2))
                elif tokens[i]=='/':
                    stack.append(int(temp2)/int(temp1))
        return int(stack.pop())
                
执行用时：44 ms, 在所有 Python3 提交中击败了87.89%的用户
内存消耗：13.8 MB, 在所有 Python3 提交中击败了16.00%的用户

