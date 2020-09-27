#43/50 暴力解超时已经是常态。。。
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container=0
        for i in range(len(height)):
            for j in range(i,len(height)):
                max_container=max(max_container,(j-i)*min(height[i],height[j]))
        return max_container


#每次看题解就会觉得自己好差劲 哎 别人为什么会这么聪明
#双指针法 每次只移动短板
#面积S=（j-i)*min(height[i],height[j])
#每次移动 j-i一定会减小 若移动长板，min（）的值只会不变或者更小！ 那么面积s一定会变小
#若移动短板，min值会变大（当然也会变小啦） 

#另个角度理解 假设i的板子更短 下一个计算s(i+1,j) 省略了s(i,j-1) s(i,j-2)...s(i,i+1)的计算 这些被省略的都是一定比当前的s更小的
#因为省略的这些 底边j-i一定会更小 高度只会更小或者不变
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container=0
        i, j=0, len(height)-1 #双指针
        while(i<j):
            max_container=max(max_container,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_container
'''执行用时：
60 ms, 在所有 Python3 提交中击败了93.40%的用户
内存消耗：
14.6 MB, 在所有 Python3 提交中击败了92.34%的用户'''
