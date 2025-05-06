# 求一棵树里面有多少个nodes
def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        这题有多种解法,bsf,preorder,backorder都可以但是这些都需要o(n)的时间复杂度,因此这题考察的是完全二叉树的性质,如果是底部满节点的完全二叉树,
        那么该树的节点计算公式为 2**depth -1.另外即使现在这棵树不是完全二叉树,我们不断往下递归的话他肯定是一颗完全二叉树. 那么如何判断一棵树是不是完全二叉树呢？如果左子树的深度等于右子树的深度
        """
        # preOrder
        if not root:
            return 0
        nodes = 0
        def preOrder(root):
            nonlocal nodes
            if not root:
                return 0
            nodes+=1
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return nodes
        # with perks for perfect tree
        if not root:
            return 0
        count =1
        left = root.left; right = root.right
        while left and right:
            count+=1
            left = left.left
            right = right.right # 根据完全二叉树的特性,如果最右边的节点depth和最左边一样,那么就是完全二叉树
        if not left and not right: #如果left和right同时到达leaf的话就是完全二叉树
            return 2**count-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right) # 1是root节点,然后两个递归分别代表两个子树