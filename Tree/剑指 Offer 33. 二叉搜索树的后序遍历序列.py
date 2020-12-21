后序遍历是左-右-根 从最后一个位置也就是根开始，对前面位置进行划分，小于根的在左子树，大于根的在右子树
以第一个大于根的位置划分，保证了左边都小于根，再检查右边是否都大于根
满足，则递归检测下一次划分
不满足，则return False
return p==end and recur(start, mid-1) and recur(mid, end) 
p==end判断此树是否正确，recur(start, mid-1)判断左子树是否正确， recur(mid, end)判断右子树是否正确
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def recur(start, end):
        这里为什么是>=而非==，在start = mid = end-1 也就是左子树为空的情况？ start mid-1 满足start>mid-1
            if start>=end: return True
            p = start
            while postorder[p]<postorder[end]: p+=1
            mid = p
            while postorder[p]>postorder[end]: p+=1
            if p==end:
                #return recur(start, mid-1) and recur(mid, end)
                这里好重要呀，根结点不要再参与下一层递归了！
                return recur(start, mid-1) and recur(mid, end-1)
            else:
                return False
            #return p==end and recur(start, mid-1) and recur(mid, end)
        return recur(0, len(postorder)-1)
执行用时：40 ms, 在所有 Python3 提交中击败了75.10%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了5.03%的用户

将后序序列变为倒序，则为根-右-左
如果当前值比上一个位置递增，那么当前值只可能是上一个值的右子树的根节点
如果是递减，那么当前值一定是之前某个root的左节点（应该不是上一个值的，根-右-左，在左才会递减，上一个应该是右而非根），root为当前值之前出现的，大于当前值的，最接近当前值的节点
          当前值右边的值，一定都小于当前值的root。因为右边的都是当前值的左右子树/为root的父节点或更高层父节点的左子树的各节点，当前值小于root，左右子树也会小于root。
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/
遍历后序遍历的倒序，遇到递减的，就判断是否满足小于root，都满足则为二叉搜索树；递增没啥限制条件，只可能是上一个数的右节点，root就是上一个数
递减的话，root是之前的数里，大于当前值里的最小数。

借助单调栈来实现，保存递增的节点，遇到递减的就出栈更新root，遇到大于当前值的就出栈！一直出！因为比当前值大的最小数在最前面！
到第一个大于当前值的点就是root
也就是单调栈里只保存了递增序列，
root只在当前值为递减的时候，更新当前值的root
当前值后面的所有值都要小于root。不然就return False
class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        stack, root = [], float('inf')
        for i in range(len(postorder)-1,-1,-1):
            if postorder[i]>root: return False
            while stack and postorder[i]<stack[-1]:
                root = stack.pop()
            stack.append(postorder[i])
        return True
执行用时：24 ms, 在所有 Python3 提交中击败了99.85%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了5.03%的用户

