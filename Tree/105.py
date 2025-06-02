# 通过前序和中序来构建二叉树
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        这题的思路和106是一样的,只不过是通过前序和中序来构建tree.思路是先通过preorder的第一个节点来找到root节点，然后根据这个value来再中序进行切割,然后根据inorder_left和inorder_right的长度来切preorder
        1)先再preorder找到root节点,然后在inorder确认root的index 2)根据root的index对inorder进行分割,这样左右子树的节点就分离出来了,3）根据inorder里面分离出来的两个数组的长度对prdorder数组
        进行分割 4)进行递归来更新root.left 和root.right的值. 5）当preorder为空时我们知道到了叶子节点这时触发return, 
        """
        if not preorder:
            return 
        #construct root and find the separator
        root_val = preorder[0]
        root = TreeNode(root_val)
        separator = inorder.index(root_val)
        # separate the inorder_left and inorder_right
        inorder_left = inorder[:separator]
        inorder_right = inorder[separator+1:]
        #separate the preorder based on inorder array length
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[len(preorder_left)+1:]

        root.left = self.buildTree(preorder_left,inorder_left)
        root.right = self.buildTree(preorder_right,inorder_right)
        return root