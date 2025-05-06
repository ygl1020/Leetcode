#求相邻两个节点的最小差值
def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        是用中序遍历,先把bst的元素按照顺序遍历出来,然后求相邻两个元素的最小值.用数组的话就后面直接遍历一边数组然后找到最小值就可以了.
        如果不通过数组直接用递归得到答案的话就需要定义两个全局变量了,一个是pre代表这个recurion上一个回合的node,一个是min_val代表了最小的相邻差值.
        pre需要全局变量是因为我们不是计算当前这个recursion的差而是计算当前iteration中的node和上一个iteration的差.所以我们需要上一个iteration的node的信息.如果pre不是全局变量我们就获取不了上一个回合的信息
        """
        # method 1是用数组
        if not root:
            return None
        sorted_tree = []
        def preOrder(root):
            if not root:
                return 
            left_dif = preOrder(root.left)
            sorted_tree.append(root.val)
            right_dif = preOrder(root.right)
            return
        preOrder(root)
        pre,cur,min_val = 0,1, float('inf')
        while cur <len(sorted_tree):
            pre_val = abs(sorted_tree[cur]-sorted_tree[pre])
            min_val = min(min_val,pre_val)
            cur+=1
            pre+=1
        return min_val
    
        # method 2， 直接比较中序遍历current和pre两个nodes的差,
        if not root:
            return None
        pre,min_val = None, float('inf')
        def inOrder(root):
            nonlocal pre,min_val
            if not root:
                return float('inf')
            inOrder(root.left)
            if pre:
                cur_dif = abs(root.val-pre.val)
                min_val = min(cur_dif,min_val)
            pre = root
            inOrder(root.right)
            return min_val
        res = inOrder(root)
        return res