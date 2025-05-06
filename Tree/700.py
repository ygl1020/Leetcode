#再binary search tree里面找符合val的node 然后返回他的root节点
"""
二叉搜索树是一个有序树：

若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
它的左、右子树也分别为二叉搜索树
这就决定了，二叉搜索树，递归遍历和迭代遍历和普通二叉树都不一样。

本题，其实就是在二叉搜索树中搜索一个节点。那么我们来看看应该如何遍历。
"""
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        第一次遇见binary search tree的题目,这里的每一个可能性都要return。bst的特性是root一定比左子树大,一定比右子树小.所以它是一个有序的tree
        """
        #递归法
        if not root:
            return None
        def dfs(root):
            if not root or root.val ==val:
                return root
            if root.val > val:
               return dfs(root.left)
            else:
               return dfs(root.right)
        return dfs(root)
    
        #迭代法
        while root:
            if val < root.val: root = root.left
            elif val > root.val: root = root.right
            else: return root
        return None