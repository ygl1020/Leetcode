# 求最小的深度
def minDepth(self, root):
        """
        这里使用前序和后序遍历都可以.但是后序遍历的话代码更简洁一些.关键是需要理解后序这里为什么需要两个if条件. 
        如果我们直接用 res = 1+min(left+right)当还没到leaf节点之前如果有一个子树的左子树为空,右子树不为空,我们应该继续左子树的value所以我们需要两个if两件在这里.否者的话这个min(left,right)会一直等于0 
        另外后序遍历我们是从子节点返回结果到父节点,所以我们这里是1+min(left,right), -->min(left,right)代表的是子节点的最小depth,然后root节点自己有一个depth
        
        前序的话我们要在叶子节点的时候进行最小值的计算,因为我们是前序,所以我们会需要两个变量,一个是全局的最小层数,一个是当前的层数. 另外因为是前序遍历所以在中间层我们就计算了节点,但是左右子树的depth还没被计算进去,所以我们
        从preOrder(root,1) depth从1开始
        """
        #postOrder
        if not root:
            return 0
        def postOrder(root):
            if not root:
                return 0
           
            left = postOrder(root.left)
            right = postOrder(root.right)
            if not root.left and root.right: #很重要
                return 1+ right
            if not root.right and root.left:
                return 1+ left
            res = 1+ min(left,right)
            return res
        return postOrder(root)

        #preOrder
        # 
        if not root:
            return 0
        result = float('inf')
        def preOrder(root,depth):
            nonlocal result  
            if not root:
                return
            if not root.left and not root.right: # prevent unnecessary function calls. They ensure we don't even make the recursive call if the child doesn't exist.
                result = min(result,depth)
            if root.left: # make sure we don;t visit empty node 
                preOrder(root.left,depth+1)
            if root.right:
                preOrder(root.right,depth+1)
        preOrder(root,1)
        return result  