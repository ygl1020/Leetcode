# 找出全部符合条件的路径
def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        这题两种回溯都可以写,但是需要注意我们append数组的时候是append的copy因为数组是mutable的,所以后面会发生改变，另外的话就是隐性回溯这里的path.pop是放在最后的,不需要放在if条件里面,这里每次递归都要回溯一下
        第二种写法的话是把path元素加入,counts的更行和回溯都放在if条件里面。另外要注意的是我们这里是从mather level就开始把path往里面加了,所以我们再一开始需要把root节点放进path传进getSum函数
        
        """
        if not root:
            return []
        res = []
        def getSum(root,counts,path):
            path.append(root.val)
            counts -=root.val
            if not root.left and not root.right and counts==0:
                res.append(path[::]) # error 1
            # if not root.left and not root.right and counts!=0:
            #     path.pop()
            
            if root.left:
                getSum(root.left,counts,path)
            if root.right:
                getSum(root.right,counts,path)

            # error2: we want to explore all the possibilities inside the tree, so we need to pop out the path like backtrackingh
            path.pop()
        getSum(root,targetSum,[])
        return res
        

        #method 2 visible backtracking
        if not root:
            return []
        res = []
        def getSum(root,counts,path):
            if not root.left and not root.right and counts==0:
                res.append(path[:]) # we need to save the copy since list is mutable thing 
            if root.left:
                path.append(root.left.val) 
                counts -=root.left.val
                getSum(root.left,counts,path)
                counts +=root.left.val
                path.pop()
            if root.right:
                path.append(root.right.val)
                counts -=root.right.val
                getSum(root.right,counts,path)
                counts +=root.right.val
                path.pop()
        getSum(root,targetSum-root.val,[root.val]) # over here, we need to pass the initial root inside the array into the getSum function, since we add the root from parent
        return res