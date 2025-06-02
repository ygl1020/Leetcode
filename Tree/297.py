
#用两个函数分别把一个tree serialize成字符串, 然后做deserialization
def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        创建一个数组用来存储preorder里面的node的值,后面用','把这个数组串起来变成一个字符串
        """
        res = []
        def preOrder(root):
            if not root:
                res.append('N')
                return
            res.append(str(root.val))
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return ','.join(res)
        

def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    创建一个全局变量self.i用来表示我们遍历字符串分解后数组的index,遇见'N'我们就return,否者就新建一个treenode,然后通过递归添加它的左右节点
    """
    self.i =0
    var = data.split(',')
    # print(var)
    def preOrder():
        if var[self.i] == 'N':
            self.i+=1 #即使是遇见空的值我们全局变量self.i 也要加1,否者后面回溯的时候这个值就出错了
            return None
        # print(self.i)
        root = TreeNode(val=int(var[self.i]))
        self.i+=1
        root.left = preOrder()
        root.right = preOrder()
        return root
    return preOrder()