#给定两个tree,然后把这两个tree进行结合,如果node.val相同就相加,如果有一个node.val是空那么就用两个node的值
def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        这题可以用前序遍历,两棵树都走到了叶子节点开始开始return, 递归逻辑为当两个node的val,把这个node变为空,否者的话把节点的vals相加.然后进行左右节点的递归 
        这题有两个需要注意的点,分别在于keypoint1和keypoint2. 
        1 保证的是再当前递归回合,我们进行node.val取数时不会出错,因为如果取none.val会报错
        2 保证的是再递归的进行是如果遇见none.left的情况不会出错,如果是none那么就会直接取none而不是none.left.val. 因为再进入递归之前python会先把none.left.val的值先取出来,所以递归里面的if在这里是没用的,我们需要额外的一个if来确保递归式的正确性
        """
        if not root1 and not root2:
            return 
    
        # Keypoint check 1 Get the values of the nodes, defaulting to 0 if the node is None
        val1 = root1.val if root1 else 0 # Handles value access for the current node only and Prevents AttributeError when reading .val
        val2 = root2.val if root2 else 0
        
        # Create new node with the sum of values
        newRoot = TreeNode(val1 + val2)
        
        # Recursively merge left and right subtrees
        #Keypoint check 2
        newRoot.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None) #Handles tree traversal to child nodes and Prevents AttributeError when accessing .left/.right
        newRoot.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        
        return newRoot