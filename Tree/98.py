#p判断一个tree是否是二叉搜索树.
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    """
    首先要明确二叉搜索树的定义是什么.假设一个二叉搜索树具有如下特征：
                                                              1: 节点的左子树只包含小于当前节点的数。
                                                              2: 节点的右子树只包含大于当前节点的数。
                                                              3:所有左子树和右子树自身必须也是二叉搜索树。
    这题我出现了很多的问题：
    1)是否需要用回溯: 这题我们不需要回溯,因为对比pathSum的问题,我们在pathSum当中有一个全局的变量counts.这个counts是根据每一个节点的值来改变的并且我们需要在每一个leaf节点返回counts之前的值来进行下一个子树的搜索
                     但是这题的话我们只需要根据父节点来更新子节点的lower和upper的值,这并不设计一个全局变量的因素
    2)如果是用前序遍历为什么return要放在后面: 前后中序的遍历只是根据处理节点操作的顺序而定的,return的位置并不能最为前中后序的决定因素.因为并不是说前序的return一定要在最前面.这里我们需要确保左右子树都是二叉搜索树才能
                                           知道整个tree是否是二叉搜索树.因此是在最后对左右两个结果进行合并再return
    3)在前序遍历中为什么lower和upper的值不是固定的?它是怎么改变的:再递归的过程中根据当前的root函数,我们直接把子节点的参数进行更新
    4)这里可以用前中后三种顺序解题吗? 可以的.如果是前序的话我们就需要定义一个区间，然后这个区间是动态改变的的,我们判断当前的节点的值是否再这个区间之内来判断它是否符合二叉搜索树的条件
                                    如果是中序遍历的话,我们只需要判断这个左子树的最大值是否是小于当前的node.val.因为这是二叉搜索树的特性来的.我们可以保证如果这个树是二叉搜索树,那么它的中序遍历的val一定是单调递增的
                                    .因此我们需要定义一个全局遍历maxVal代表访问过的全部node中的最大值.如果下一个node的值小于或等于这个值就说明这个tree不是二叉搜索树.注意这里的maxVal一定要是全局变量,如果缺少了nonlocal的话maxVal的值只会再
                                    局域函数里面进行变化而再全局的值还是保存一样的
    """
    #method 1, preorder solution . need upper and lower bond
    if not root:
        return False
    def dfs(root,lower,upper):
        if not root:
            return True
        cur = root.val
        if cur <=lower or cur >=upper:
            return False
        left_res = dfs(root.left,lower,cur)
        right_res = dfs(root.right,cur,upper)
        return left_res and right_res
    return dfs(root,float('-inf'),float('inf'))

    #method 2, inorder, only need a golbal maxVal
    maxVal = float('-inf')
    def inOrder(root):
        nonlocal maxVal
        if root is None:
            return True

        left = inOrder(root.left)
        # 中序遍历，验证遍历的元素是不是从小到大
        if maxVal < root.val:
            maxVal = root.val
        else:
            return False
        right = inOrder(root.right)

        return left and right
    return inOrder(root)


    """
    另外我错误的原因是我只是单纯的比较左右节点但是bst是需要每一层的root都把左节点大比右节点小
    这题我的思路是用中序遍历,因为根据bst的特性,根节点值一定是大于左节点的并且小于右节点的.因此如果是中序遍历的话我们一定可以得到一个单调递增的函数,
    method 3这样的话我们只需要定义一个全部变量
    minimum来记录上一个节点的值,然后再中间把当前节点的值和这个minimum进行比较.如果是bst,那么每次root.val一定是大于minimum的.否者就不是bst 我们可以return false. 最后我们需要保证
    左右两个分分支树都return true才可以判断这个tree就是bst.但是这样写有一个隐患,如果第一个左叶子的值就是负无穷的话我们的策略就行不通了,因为我们直接就return false了
    method 4更好的优化是定义一个pre全局变量来记录上一个node的值,然后把这个pre和current root的值进行比较.
    
    """
    #method3
    # if not root:
    #     return True
    # minimum = float('-inf')
    # def postOrder(root):
    #     nonlocal minimum
    #     if not root:
    #         return True
    #     left = postOrder(root.left)
    #     if root.val >minimum:
    #         minimum = root.val
    #     else:
    #         return False
    #     right = postOrder(root.right)
    #     return True if left and right else False
    # return postOrder(root)
    #method4
    if not root:
        return True
    pre = None
    def postOrder(root):
        nonlocal pre
        if not root:
            return True
        left = postOrder(root.left)
        if pre is not None and pre >=root.val:
            return False
        pre =root.val
        right = postOrder(root.right)
        return True if left and right else False
    return postOrder(root)
    #method 5
    """
    method4 用前序遍历,思路在于我们只需要保证每一个节点都再固定的范围内,如果该节点不再固定的范围内,那么可以直接return false.否者我们需要继续往下遍历剩余的node,如果往左遍历
        那么我们就需要更新右边界为当前节点的value保持左边界不变,如果是往右遍历,那么我们应该更新左边界为当前node的value然后保存右边界不变.最后如果左右子树都return true我们就可以
        判断这个tree是bst
    """
    def vaild(root,left,right):
            if not root:
                return True
            if root.val <=left or root.val >= right:
                return False
            return vaild(root.left, left, root.val) and vaild(root.right, root.val,right)
    return vaild(root, float('-inf'), float('inf'))
    