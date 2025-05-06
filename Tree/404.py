#求所有左叶子节点的和
def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        这题我一开始的思路使用前序遍历,但是前序遍历有一个问题,我们可以收集leaf的值但是我们并不知道这个leaf是不是左叶子还是右边的叶子,因为最好的办法是用后序遍历-->我们先手机左边子树的value和右边子树的value.
        然后把这两个value进行相加来得到需要的值.所以使用递归三部曲的话1) 我们需要root参数,函数返回的是integer 2)我们再这题是再叶子节点之前就收集到了左叶子的信息,因为我们return的停止条件是a: not root return 0 b: if not root.left and not root.right return 0 3)在单层递归逻辑里,我们如果遇见左叶子要进行收录
    
        """
        # method1 postorder recursion
        if not root:
            return 0
        def addLeft(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 0
            leftV =addLeft(root.left)  # left 下面虽然有一些logic但是这个logic不是属于mid的logic
            if root.left and (not root.left.left and not root.left.right): 
                leftV += root.left.val
            rightV = addLeft(root.right) # right
            total = leftV+ rightV # mid
            return total
            total = addLeft(root.right)
            return left_value
        total = addLeft(root)  
        return total 
        # method2 inorder recursion
        """
        所以这就是递归的前后遍历的差异化吗,如果用前序遍历我们不知道左右子树的值,我们只有先把符合要求的值进行收集然后再把这个变量和后面左右子树的值进行累加,因此我们要用total +=addLeft(root.left)  
        total += addLeft(root.right). 在后序遍历中我们是先计算左子树和右子树的值,最后我们把左右子树的vlaues相加得到最后的值
        """
        if not root:
            return 0
        def addLeft(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 0
            total = 0
            if root.left and (not root.left.left and not root.left.right):
                total +=root.left.val
            total +=addLeft(root.left)  # left 下面虽然有一些logic但是这个logic不是属于mid的logic
            total += addLeft(root.right) # right
            return total

        return addLeft(root)  
    
        #method3 iteration 因为是用stack所以左右的顺序是反过来的 ,这里注意用迭代和递归两个方式的区别
      
        if root is None:
            return 0
        st = [root]
        result = 0
        while st:
            node = st.pop()
            if node.left and node.left.left is None and node.left.right is None: #mid的逻辑
                result += node.left.val
            if node.right: #right
                st.append(node.right)
            if node.left: #left
                st.append(node.left)
        return result
    
    """
    我把404和112进行了对比 以下是一些总结
    1. 问题目标驱动设计差异
    路径总和:目标是存在性判断,需遍历所有可能的路径,并在过程中维护路径的累加状态(counts)。递归需要显式回溯以尝试不同分支。

    左叶子之和：目标是属性统计，只需识别特定节点（左叶子）并累加其值。递归通过返回值自底向上累加结果，无需中间状态管理。

    2. 递归参数与状态管理
    路径总和：

    传递剩余目标值(counts),进入子节点时修改参数,返回时需恢复(回溯)以尝试其他路径。

    状态（剩余值）与递归调用强绑定，父子递归间存在显式状态传递。

    左叶子之和：

    无额外参数，仅通过递归返回值传递子树的左叶子总和。

    状态（总和）隐含在返回值中，父子递归间通过返回值直接累加。

    3. 回溯的必要性
    路径总和：必须显式回溯。因需遍历所有路径，递归进入左/右子节点后若未找到解，需撤销状态修改以尝试其他分支。

    左叶子之和：无回溯。每个节点独立判断左子节点是否为左叶子，递归结果直接累加，无需撤销任何操作。

    4. 判断逻辑的时机与主体
    路径总和:在叶子节点判断剩余值是否为0,由叶子自身决定是否满足条件。

    左叶子之和：在父节点判断其左子节点是否为叶子，由父节点决定是否计入统计。

    5. 递归类型与返回值作用
    路径总和:类似深度优先搜索(DF).返回值是布尔值,通过逻辑短路(if getSum(...): return True)快速终止递归。

    左叶子之和：类似后序遍历（左右根），返回值是数值，通过左右子树结果的直接相加完成统计。

    核心思想
    路径总和：递归是主动探索的过程，需要维护路径状态并管理回溯。

    左叶子之和：递归是被动收集的过程，通过返回值隐式传递结果。
    
    
    
    """