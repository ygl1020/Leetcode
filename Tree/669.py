# 在bst里面把不在range里面的node全部删去然后返回最新的root
def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        这题和450的解题思路有点不太一样,因为我们在450只需要删除一个节点就可以,所以我们可以把情况具体分为5种.这里的话我们如果找到root.val 是<low 那么我们知道需要把该节点删除,但是我们还需要判断该节点的右子树是否存在不符合范围的节点,
        因此我们把该节点的右子树当成一个独立的tree然后再次进行一次回溯. 同理可得当root.val>high 的情况. 这里需要知道的是我们在top return里面return的值是处理过之后的新的root,然后这个root会被返回到被删除节点的父节点作为分节点
        """
        if not root:
            return root
        if root.val < low:
            right = self.trimBST(root.right,low,high) #把被删除节点的右子树作为一个tree然后继续进行递归来删除在右子树不符合规定的node
            return right
        if root.val>high:
            left = self.trimBST(root.left,low,high)
            return left
        root.left = self.trimBST(root.left,low,high)
        root.right = self.trimBST(root.right,low,high)
        return root
        