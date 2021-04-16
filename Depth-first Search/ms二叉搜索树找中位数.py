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

