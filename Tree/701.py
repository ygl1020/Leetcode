#在bst里面找到合适的位置来插入val节点
def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        从上面的示例可以看出来,我们再每次插入新的节点时最简单的方式就是再叶子节点插入新的节点.那么这个递归函数需不需要返回值呢？root本质来说是一个inmutable的类型,所以我们最后
        再递归的过程中进行返回，否者就是插入了新的节点如果没在递归函数中进行返回,全局的root变量还是不变的的.因此我们可以确定这里的递归函数时需要返回的,返回的时一个TreeNode.L另外我们这题因为是bst所以node是有序的,我们并不需要遍历全部的nodes
        """
        def dfs(root,val):
            if not root:
                new_node = TreeNode(val=val)
                return new_node
            if val < root.val: # 当root的值不为空时,我们根据bst的特性来判断下一步应该往哪里走
                root.left = dfs(root.left,val) # 这一步很重要因为之后我们是通过这个root.left来把新加入的节点插入到root节点的
            if val >root.val: 
                root.right = dfs(root.right,val)
            return root
        return dfs(root,val)
    
        """
        这里我原本是想在叶子节点的时候插入新节点的,因为我的想法是如果再空节点插入新的节点我们不知道是插入左节点还是右节点.但是按照我的写法的话这种情况就
        处理不了了：[40,20,60,10,30,50,70], val = 25, 正确的写法应该再空节点插入新节点,然后根据root.val和val的值来判断去左边还是去右边.这样的话我们
        也不用全部node都去一遍,节点是插入左边还是右边是回溯的时候来决定的
        """
        # if not root:
        #     return root
        # def preOrder(root,val):
        #     if not root:
        #         return root
        #     if not root.left and not root.right:
        #         if root.val >val:
        #             root.left = TreeNode(val)
        #             return root
        #         else:
        #             root.right = TreeNode(val)
        #             return root
        #     if root.val <val:
        #         preOrder(root.right,val)
        #     if root.val >val:
        #         preOrder(root.left,val)
        # preOrder(root,val)