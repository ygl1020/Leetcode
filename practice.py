class TreeNode:
    def __init__(self,val, left, right):
        self.val = val
        self.left = left
        self.right = right
    def preOreder(self,root):
        if not root:
            return 
        res = []
        def dfs(root):
            if not root:
                return 
            res.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
    
    def inOrder(self,root):
        if not root:
            return root
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root)
            dfs(root.right)
        dfs(root)
        return res
    
    def postOrder(root):
        if not root:
            return root
        res = []
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            dfs(root.right)
    
            res.append(root)
        dfs(root)
        return res
    
    def preOreder_iteration(self,root): 
        if not root:
            return root
        res, stack = [], [root] 
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
    
    def PostOreder_iteration(self,root):
        if not root:
            return root
        res, stack = [], [root] 
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:  # 我们求左右中，可以先求中右左 然后把res 取反，所以这里是先取cur.right 因为stack是先进后出
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res[::-1]
    
    def inorder_iteration(self,root):
        if not root:
            return root
        res, stack = [],[]
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res