我的思路，在pop要求的顺序里的第一个元素出现之前，一直push
遇到第一个该pop的，就开始往回走判断是不是要吐出来之前吞进去的，一直吐到不再和要pop的元素相同的时候，继续下一轮的push，此时push元素的位置非常重要，是位于之前push到的元素下一个位置的元素
如果不需要吐，就继续下一轮循环

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        cur = 0 #工作指针的起始位置
        for j in pushed:
            if j!=popped[cur]:
                stack.append(j)
            else:
                cur+=1
                #其实下面这两行没必要写，就是为了不需要往前找的时候跳过后面的代码写的continue
                #写的话也不是不可以，但是要带上len（stack）>0 否则stack[-1]有时候会越界
                #比如测试用例为[0][0]/[1,0],[1,0]这种pushed和popped完全相同，每进一个就立刻出来的情况
                # if cur<len(popped) and stack[-1]!=popped[cur]:
                #     continue
                while len(stack)>0 and stack[-1]==popped[cur]:
                    stack.pop()
                    cur+=1
        return False if len(stack)>0 else True   
    
    
看题解最后一句写return not stack 感觉学到了

执行用时：36 ms, 在所有 Python3 提交中击败了97.03%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了5.29%的用户

     
        
