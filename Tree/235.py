# 再bst里面找到两个nodes的最小公共祖先
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        第一种方式用的就是后序遍历没有使用bst的特性，第二种方式的话就是我们只要找到第一个root然后root.val是在[p,q]之间的话就是最小公共祖先
        首先我们需要确定这个递归函数是有返回值的,而且这个返回值是一个TreeNode.如果我们用dfs(root.left,p,q) 和dfs(root.right,p,q) 而不记录他们的值
        """
        #method 1
        if root==q or root==p or not root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        elif left and not right:
            return left
        elif not left and right:
            return right
        else:
            None
        
         #method 2
        if q.val <= p.val: #ensure p is smaller than q
            p, q = q,p
        print(p.val,q.val)
        def dfs(root,p,q):
            if not root or (p.val<=root.val<=q.val):
                return root
            if root.val > q.val:
                return dfs(root.left,p,q)
            elif root.val < p.val:
                return dfs(root.right,p,q)
        return dfs(root,p,q)

        #method 3
        """
        这里主要是掌握第二种bfs的解法,一开始我的思路知道我们应该把后序遍历转为前序,但是我不知道当root.val再p.val和q.val之间时就可以判断它时最近的公共祖先
        另外再收到了左右两个分支子树的reutn时我们可以判断他们是否不为空,不为空就说明我们找到了最小公共祖先
        """

        if q.val <= p.val: #ensure p is smaller than q
            p, q = q,p
        if not root or (p.val<=root.val<=q.val):
            return root 
        left = self.lowestCommonAncestor(root.left, p,q)
        if left:
            return left
        right = self.lowestCommonAncestor(root.right,p,q)
        if right:
            return right