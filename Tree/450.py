#在一个bst中找到一个node并删除它
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        第一种情况：没找到删除的节点，遍历到空节点直接返回了
        找到删除的节点
        第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
        第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
        第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
        第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。
        我们这题的递归函数是有返回值的,返回值为treenode类型.所以我们在最上面的return 情况需要返回更新后的root节点. 这个节点在后面会被返回给对应的左子树或者右子树
        """
        if not root: #这里注意第一个if not root就是处理没找到删除节点时以及空节点的情况,
            return root
        if root.val ==key:
            if not root.left and not root.right:
                return None
            elif root.left and not root.right:
                root = root.left
                return root 
            elif not root.left and root.right:
                root = root.right
                return root 
            else:
                cur = root.right
                while cur.left:  # error 1 在这里应该遍历到root的右子树的最后一个left node为止.因为只要这个left node的节点值是最靠近root左子树的,所以是while循环 cur.left而不是cur. 因为我们要保证cur.left有值
                    cur = cur.left 
                cur.left = root.left
                root = root.right   # 再遇见删除节点左右都不为空时,最后记得吧root=root.right
                return root
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        if root.val <key:
            root.right = self.deleteNode(root.right,key)
        return root