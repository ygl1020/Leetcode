#145
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #method 1, 使用递归,相较于preorder，我们只要调换res.append(root.val)从dfs(root.left)之前到dfs(root.right)之后就可以了
        if not root:
            return []
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res

        """
        method 2，在实现preorder时,我们需要处理的顺序时中左右，对于postorder我们需要左右中,如果我们在入栈时调换处理右子节点和左子节点的顺序-->preorder中是先右节点入栈,然后左节点入栈,这题我们改为先左节点入栈,然后右节点入栈.
        最后我们的结果就会变成中右左, 相比要求的左右中,我们只需要讲当前数组进行反转就好了
        """
        if not root:
            return []
        res =[]
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
    