#通过中序和后序构建数组
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        通过中序和后序两个数组来构建二叉树,我们先通过postorder的最后一个元素找到root节点,然后通过这个节点再inorder的为止来切成inorder_left和inorder_right.之后我们回到postorder继续进行切割.因为中序和后序的array长度一定是相等的,所以切后序的时候可以用inorder_left和inorder_right来直接切.
        最后我们通过递归来不断切下去获得左子树和右子树的值.当后序数组里面没有值时就说明根节点出现了.我们结束递归
        """
        if not postorder:
            return 
        # constuct root and find the separator
        root_val = postorder[-1]
        root = TreeNode(root_val)
        sperator = inorder.index(root_val)

        # sperate inorder
        inorder_left = inorder[:sperator] #取到root_val的值之前的位置,不包括root_Val
        inorder_right = inorder[sperator+1:] #root_val之后一个值一直到最后一个element

        #separate postorder based on inorder length
        postorder_left= postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root