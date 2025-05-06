#144
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        用递归非统一写法的话可能面试的时候更容易进行讲解,具体思路是创建一个stack[root]和res[]数组,然后因为是前序遍历,因为每次我们先把stack里面最新加入的元素出栈(代表我们处理的了这个root节点),然后放入res里面. 
        之后话看出栈的元素是否有左右子节点,有右节点的话先把右节点入栈!!这个很重要因为出栈的顺序是反过来的,要实现中左右,那就需要先把右节点入栈,如果左节点先入栈那就是右节点先出栈,这样顺序就错了. 
        因此我们需要用while:stack来进行迭代
        """
        if not root:
            return []
        res= []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left: # 这里一定要用if而不是elif, 如果if node.right 返回true那么elif就会被忽略导致错过左节点的入栈
                stack.append(node.left)
        return res
    
      