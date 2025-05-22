#再一个tree里面找到是否存在一个子节点等于另一个tree
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    首先把问题理解为,再一个tree里面找是否有子树等于里另一个tree.那么我们就是先对比头节点和子树,不相等就继续对比头节点的左右子树.这个是一个递归的过程,一直到找到子树或者遍历了全部子节点为止
    这个过程中我们需要一个helper 函数sameTree来对比当前子节点和子树是否相等-->如果两个数都为空那就return True,如果只有一个树为空或者两个树都不为空但是值不相等那么就是return False.否者
    我们继续对比两个数的其他子节点. 再isSubTres函数中,如果subRoot为空,那么我们不用对比直接return True,之后如果root为空,那么当subroot不为空时-->不可能找到子树return False
    在递归的过程中如果当前root的子节点和subRoot相同,那么就直接return True,否者我们继续递归遍历root的其他子节点的情况
    """
    if not subRoot:
        return True
    if not root:
        return False
    if self.sameTree(root,subRoot):
        return True
    return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

def sameTree(self,r,s):
    if not r and not s:
        return True
    if not r or not s or r.val != s.val:
        return False
    return self.sameTree(r.left,s.left) and self.sameTree(r.right, s.right)