# 根据一个tree来找到postOrder的数组
def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        这题其实是144的变种,preOrder是中左右,postOrder是左右中所以我们先找到中右左 然后把数组反转就可以了
        """
        # method1
        # res = []
        # if not root:
        #     return []
        # def postOrder(root):
        #     if not root:
        #         return 
        #     postOrder(root.left)
        #     postOrder(root.right)
        #     res.append(root.val)
        # postOrder(root)
        # return res

        #method 2
        if not root:
            return []
        stack,res = [root], []
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.left: # 因为stack是先进后出的顺序,因此要中右左需要先遍历左节点
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res[::-1]