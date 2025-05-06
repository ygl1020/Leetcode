#94
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # method 1 recurive
        if not root:
            return []
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

        #method 2< iteration
        """
        迭代的中序遍历和前序遍历不一样,前序的遍历是中左右所以我们处理root节点和遍历的顺序是相同的,但是中序遍历是左中右,我们要先遍历到根部的左节点,然后开始处理节点.因此我们并不可以直接通过修改
        前序遍历的迭代代码来处理中序遍历.在这里我们需要使用一个指针来帮助我们实现这个遍历的过程具体的思路是1)先用指针一直向下走到最下面的左边的子节点,这个过程中路过的node入栈,这种情况的话访问的指针一定是非空值
        2) 然后到达底部的左节点时我们开始向节点的右边搜索,先把最后一个元素出栈,然后记录当前元素-->放入res数组,之后重新定义指针为当前元素的right节点-->这种情况指针一定为空
        3）当我们遍历完左边的全部节点，栈为空但是指针是指向root节点的右节点的.最后全部node遍历完stack和指针皆为空.因此while循环的条件是while cur or stack
        """
        if not root:
            return []
        res= []
        stack = [] # 注意这里我们先不把root入栈
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()  # 这里要注意出栈的命名是指针的名字,否者我们就没有更新指针会出错
                res.append(cur.val)
                cur = cur.right
        return res