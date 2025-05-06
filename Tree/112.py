#这题是要求是否有路径存在,路径的和会等于target
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        这题可以用两种回溯的方式写,第一种的话是隐式回溯-->我们先把减去node.val,然后我们做后续的判断,因为这样我们使用counts的方式对于全局来说是一致的所以我们不需要进行counts的revert
        第二种回溯方式是在进行左右子树的递归时,因为每一个循环分支里面的counts值不一样所以我们需要分别处理-->把它进行revert当getSum()的返回值时false时.eg当遍历完一条左路径后我们没有找到符合条件的路所以我们需要走右路径.这时我们要先把再左路径减去的值加回来
        """
        # invisible backtrakcing
        if not root:
            return False
        def getSum(root,counts):
            counts-=root.val
            if not root.left and not root.right:
                return counts==0
            if root.left:
                if getSum(root.left,counts):
                    return True
            if root.right:
                if getSum(root.right,counts):
                    return True
            return False
        return getSum(root,targetSum)
    
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # visible backtracking: the counts will be modified for each recursion case, so we do the modifcaitons before enter the recursion and revert the counts if the return is False
        if not root:
            return False
        def getSum(root,counts):
            if not root.right and not root.left and counts==0:
                return True
            if not root.right and not root.left and counts!=0:
                return False
            if root.left:
                counts -= root.left.val
                if getSum(root.left,counts):
                    return True
                counts+= root.left.val
            if root.right:
                counts -= root.right.val
                if getSum(root.right,counts):
                    return True
                counts+= root.right.val
            return False
        return getSum(root,targetSum-root.val)