#在一个tree里面找到众数，然后把所以的众数的值放入一个array
def findMode(self, root: Optional[TreeNode]) -> List[int]:
        """
        一开始我的想法是用递归先把tree遍历一遍,然后把每一个value放在一个字典里.之后我们遍历字典找到出现频率最多的次数.然后遍历字典找到出现频率等于最大次数的value.但是这样的话就没有利用bst的特性.
        在这里我们可以使用中序遍历,然后设计res,maxCount, count,pre 四个全局变量.res代表最后出现次数最多的数字,maxcount代表最多的出现频率，count代表当前这个value出现的次数.然后pre代表上一个node的value。
        我们先更新counts分为三种情况 1)pre is none-->初始的情况, 2)pre ==cur 3)pre!=cur 然后更新pre,之后更新maxcounts和res的值
        
        这题我知道是用中序遍历,通过对比counts和max_counts的值来找到mod.但是我具体的逻辑没有搞清楚因此出错了.因为肯定是先确认counts和max_counts的关系,然后再去更新res和max_counts
        """
        #method1
        if not root:
            return []
        pre,count,maxCount,res = None,0,0,[]
        def inOrder(root):
            nonlocal pre,count,maxCount,res
            if not root:
                return 
            inOrder(root.left)
            if not pre:
                count =1
            elif pre.val == root.val:
                count+=1
            else:
                count =1
            if count == maxCount:
                res.append(root.val)
            if count > maxCount: # 当出现count大于maxCount时我们需要更新maxCount并且把res的值清空然后把当前的root加进去
                maxCount = count
                res = [root.val] 
            pre = root
            inOrder(root.right)
        inOrder(root)
        return res
    
        #method2
        if not root:
            return []
        max_counts,res,counts,pre= 0,[],0,None
        def inOrder(root):
            nonlocal max_counts,counts,pre,res
            if not root:
                return
            inOrder(root.left)
            if pre and pre.val == root.val: # 当pre不为空,并且pre的值和当前的值是相等时我们把counts的值加1
                counts += 1
            else:
                counts = 1 #当pre为空或者pre的值和当前值不相等时,把counts从1开始更新
            if counts == max_counts:
                res.append(root.val)
            elif counts > max_counts:
                max_counts = counts
                res = [root.val]
            pre=root
            inOrder(root.right)
        inOrder(root)
        return res