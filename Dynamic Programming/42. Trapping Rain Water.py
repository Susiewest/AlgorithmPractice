基础的做法，针对每个位置i，如果左右两边的最大柱子都比自己大，那么位置i就可装min（左，右）-自己的高度个水
但是每次找左右最大柱子复杂度很高，所以用两个数组两次遍历动态规划保留每个位置左右的最大柱子

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        maxleft = [0]*n
        maxright = [0]*n
        maxleft[0] = height[0]
        maxright[-1] = height[-1]
        result = 0
        for i in range(1, n):
            maxleft[i] = max(maxleft[i-1], height[i])
        for j in range(n-2, -1, -1):
            maxright[j] = max(maxright[j+1],height[j])
        for k in range(n):
            if min(maxright[k],maxleft[k])>height[k]:
                result += min(maxleft[k],maxright[k])-height[k]
        return result
      
执行用时：44 ms, 在所有 Python3 提交中击败了79.96%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了18.25%的用户

转为双指针法，设置left right两个指针遍历，maxleft和maxright取较小值计算当前left/right的高度差，如果当前高度就是最大，那减掉就是0，如果有差就加入总和计数 left++/right--

