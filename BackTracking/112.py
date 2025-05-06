#这题是要求是否有路径存在,路径的和会等于target
def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        def getPath(root,counts):
            if not root.left and not root.right and counts ==0: #if at lead counts != 0, path value is equal to targetSum
                return True
            if not root.left and not root.right and counts !=0:
                return False
            if root.left: 
                counts-=root.left.val
                if getPath(root.left,counts):
                    return True
                counts +=root.left.val # 
            if root.right:
                counts-=root.right.val
                if getPath(root.right,counts):
                    return True
                counts +=root.right.val
            return False
        return getPath(root, targetSum - root.val)    

        if root is None:
            return False
        def getPath(root, counts):
            counts -= root.val  # ✅ do it early as you wanted

            # ✅ base case adjusted
            if not root.left and not root.right:
                return counts == 0

            if root.left:
                if getPath(root.left, counts):
                    return True

            if root.right:
                if getPath(root.right, counts):
                    return True

            return False

        return getPath(root, targetSum)
    