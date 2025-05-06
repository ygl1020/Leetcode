# 根据一个有序数组构建平衡bst
def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        这题我有一点思路,但是对具体细节的把握还是不够,我想到了我们需要在中间不断的取medium元素创建新的node,然后根据medium的值对nums不断进行左右的分割来进行递归一直到分割好的数组里面是空的.这时我们就return none代表该方向的全部element都分配完了.
        这里不可以用if not nums: return root   因为root是local variable所以在当前的递归中我们不知道它的值,因此是返回none. 另外的就是我们root.left的结果是接在root这个节点最为子树的.题目450之前的话是把修改后的新节点root的return到原根节点的父节点上.这两题的root衔接顺序是不一样的
        """
        if not nums: # 因为root是local variable所以我们这里没有root的信息 不能return root
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid]) # 根据bst的性质 左边的子树一定小于root,因此把mid左边的值放入下一个递归回合
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    
    
