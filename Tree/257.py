# 求root到leaf的全部路径
def binaryTreePaths(self, root):
        """
        这题求的是从root到leaf节点的全部路径,所以用前序遍历比较合适.因为我们中左右先root节点然后到最左的leaf节点,之后回溯探索下一个路径
        这题的回溯可以有多种写法.第一种是显式的回溯,也比较好理解.根据题目的意思我们需要两个array,一个是res一个是path用来记录每一次的路径点.因此我们到达根节点就把path添加到res里面并触发返回.
        那么在叶子节点的过程中遇见空节点怎么办呢.这个情况我们通过if root.right 和root.left来跳过空节点.并且我们需要在每一次递归结束都需要进行回溯-->path是数组因此是mutable的.
        如果在leaf是path是1,2,5那么我们在把结果返回给节点2时需要删除节点5,然后再继续探索新的节点.  
        第二种写法是invisible的回溯,我们把path传递到下一层的递归是传递的是一个浅拷贝,因此下层的path结果return到上一层的时候path其实是没有被改变的,
        所以我们其实不需要回溯的过程.因为path的value再子节点的改变不会影响当前层的path值
        
        """
        # preOrder visable backtracking
        res,path = [],[]
        if not root:
            return []
        def preOrder(root,res,path):
            path.append(root.val)
            if not root.left and not root.right:
                tmp_path = "->".join(map(str,path))
                res.append(tmp_path)
                return
            if root.left:
                preOrder(root.left,res,path[:])
                # path.pop()
            if root.right:
                preOrder(root.right,res,path[:])
                # path.pop()
        preOrder(root,res,path)
        return res

        # preOrder invisable backTracking
        res,path = [],[]
        if not root:
            return []
        def preOrder(root,res,path):
            path.append(root.val)
            if not root.left and not root.right:
                tmp_path = "->".join(map(str,path))
                res.append(tmp_path)
                return
            if root.left:
                preOrder(root.left,res,path[:]) # 传输的是path的浅拷贝,所以下一层的递归对path的改变其实对上一层的path的值没有影响.简答说的话就是传递了一个新的path给下一层.但是这样占据了更对的储存空间
                # path.pop()
            if root.right:
                preOrder(root.right,res,path[:])
                # path.pop()
        preOrder(root,res,path)
        return res
