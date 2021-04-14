ms笔试

像素渲染 打包成tuple，sort，从小到大排序，贪心记录最多渲染多少

节点之间的权值最大，算每个点的入度出度和，大的代表参与的路径多，贡献大，为了让总权值最大，就把大的权值赋给这种节点，也相当于贪心了？

数组中切两刀成三个链，求切的cost最小，用了三个方法，一暴力，二双指针，大的一个指针挪动， 三构建大根堆，除去开头结尾 挑出来四个最小的数，两两结合验证下标是否符合相差大于1
第三题有个测试用例没过，经过我思考，应该是遗漏了处理 数组长度为5的边界情况，这样必须选第二个数和第四个数，而不能按照上面的思路构造大小为4的堆！

bst找中位数，空间复杂度O（1） 时间复杂度O（n）

class Node():
    def __init__(self, value, left, right):
        self.val = value
        self.left = left
        self.right = right
class Solution():
    def __init__(self):
        self.node_num = 0
        self.count = 0
        self.result = -1

    def inorder(self, root, target):
        if not root:
            return
        self.inorder(root.left, target)
        self.count += 1
        if self.count == target:
            self.result = root.val
        self.inorder(root.right, target)

    def bst(self, root):
        if not root:
            return False
        def dfs(root):
            if not root:
                return
            self.node_num += 1
            dfs(root.left)
            dfs(root.right)
        dfs(node1)
        if self.node_num%2:
            target = self.node_num//2 +1
        else:
            target = self.node_num//2
        self.inorder(root, target)
        return self.result

node1 = Node(4, None, None)
node2 = Node(2, None, None)
node3 = Node(6, None, None)
node4 = Node(1, None, None)
node5 = Node(3, None, None)
node6 = Node(5, None, None)
node7 = Node(7, None, None)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
sol = Solution()
ans = sol.bst(node1)
print(ans)

