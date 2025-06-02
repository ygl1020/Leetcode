#在一个tree里面同一个节点不能经过两次,求最大路径之和
def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        这道题需要需要明确什么是合法路径,已经合法路径的最大和是怎么计算你的,这里的最大和可以分为两种 1)在当前节点split,那么它的最大和就是root节点和left已经right的和相加
        2)在当前节点不split,当前节点的最大和为root.val+max(right,left,0)因为我们需要把当前节点的符合路径的最大和return会上一层的parent节点,因此我们不可以左右两个方向都选
        另外当节点的值为负数时,我们也可以不选该节点因此我们把0也放入max函数里面.
        另外max(res[0],max_split) 不需要把max_Nsplit也放进去,因为max_split已经包含了max_Nsplit的可能性-->eg inorder[20,-1,10], root为20,left为-1，right为10, 我们left的max为
        0，right的max为10,因此在root中max_Nsplit为--> 20+max(0,10,0) = 30, max_split = 0+20+10=30.
        """
        res = [root.val]
        def postOrder(root):
            if not root:
                return 0
            left = postOrder(root.left)
            right = postOrder(root.right)
            left = max(0,left) # 需要在计算max_split和max_Nsplit之前先确保如果左右node的值为负数就取0
            right = max(0,right)
            # compute for not split case
            max_split = root.val+left+right
            # compute for split case
            max_Nsplit = root.val+max(left,right)
            # update global maximum
            res[0] = max(res[0],max_split) # 这里不需要放max_Nsplit因为计算max_split时已经包含了这个可能性,
            return max_Nsplit
        postOrder(root)
        return res[0]