import collections
class TreeNode:
    def __init__(self, val= 0, left=None, right=None ):
        self.val = val
        self.left = left
        self.right = right
    def preorder_iteration(self,root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop() 
            result.append(node.val) # 先处理根节点
            if node.right: # stack是先进后出所以我们先加入右节点
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
    
    def inorder_iteration(self,root):
        if not root:
            return []
        stack = []
        result = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur) # 先遍历到左子树的leaf,然后当左leaf的一下iteration, cur= none，所以这时开始把cur.val放入res，然后到中间的node,加入node.val 之后找中间node的right子树
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result 
        
    def postorder_iteration(self,root):
        if not root:
            return 
        stack = [root]
        result = []
        while stack: # 我们按照中右左的方式先把res算出来 然后反转res得到左右中
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
    
    
    def level_iteration(self,root):
        if not root:
            return []
        queue = collections,queue([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.right)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result    
    
    
a = [9,3,15,20,7]
b = [9,15,7,20,3]

root_val = b[-1]
separator_idx = a.index(root_val)
inorder_left = a[:separator_idx]    
inorder_right = a[separator_idx + 1:]
postorder_left = b[:len(inorder_left)]
postorder_right = b[len(inorder_left): len(b) - 1]
print(inorder_left,inorder_right,postorder_left,postorder_right)