# 根据一个tree求出preorder的数组
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # method 1 using recursive 
        # step1: define what parameters will be used inside dfs function and what will be the return
        # step2: what will be the return condition?
        # step3: what will be the logic inside every iteration of the recursive
        res = []
        def dfs(root):
            if not root:
                return 
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

        #method 2 using iteration
        """
        用递归非统一写法的话可能面试的时候更容易进行讲解,具体思路是创建一个stack[root]和res[]数组,然后因为是前序遍历,因为每次我们先把stack里面最新加入的元素出栈(代表我们处理的了这个root节点),然后放入res里面. 之后话看出栈的元素是否有左右子节点,有右节点的话先把右节点入栈!!这个很重要因为出栈的顺序是反过来的,要实现中左右,那就需要先把右节点入栈,如果左节点先入栈那就是右节点先出栈,这样顺序就错了. 因此我们需要用while:stack来进行迭代
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
            if node.left:
                stack.append(node.left)
        return res

        #method 3 简洁的写法
        if not root:
            return 
        res = [root.val]
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res
    
        #method 4是错误的写法,因为每一次的recusion都建立一个新的res,所以之前储存的元素就丢了
        res = []
        if not root:
            return 
        res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return res