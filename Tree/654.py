#通过nums数组中的最大值构建最大root tree
def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        找到当前nums的最大值,然后按照最大值进行left_nums和right_nums的切割,一直进行下去一直到nums为空进行返回
        """
        if not nums:
            return
        root_val = max(nums)
        root = TreeNode(root_val)
        separator = nums.index(root_val)
        nums_left = nums[:separator]
        nums_right = nums[separator+1:]

        root.left = self.constructMaximumBinaryTree(nums_left)
        root.right = self.constructMaximumBinaryTree(nums_right)

        return root