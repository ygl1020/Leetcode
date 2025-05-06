# 根据高度判断二叉树是否为平衡子树的问题
def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        我的想法是因为是根据高度来判断是否是否是height_balacned tree,所以应该用后序遍历.然后当我们判断左右两个子树的高度差大于1时就所以不是高度平衡,所以可以直接返回False
        这里很巧妙的利用了后序结果向上传递的原理,当我们判断当前的root的左右子树高度差大于1,return -1,
        然后这个-1被返回到当前root的父节点,因此我们可以判断if left == -1 or right == -1 or abs(left - right) > 1 return Fasle
        """
        if not root:
            return True
        def postOrder(root):
            if not root:
                return 0
            left = postOrder(root.left)
            right = postOrder(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1: # 当abs(left-right)>1时会返回-1,然后-1的结果传递到上面的父节点因此left 或者right出现了-1就直接return -1
                return -1
            res = max(left, right) + 1
            return res
        return postOrder(root) != -1