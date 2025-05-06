#给你一个数字n求再n中抽取k个数字,有几种抽发,然后返回所有的可能性
def combine(self, n: int, k: int) -> List[List[int]]:
        """
        递归三部曲：1）返回值是什么以及需要什么参数：
                      一般的回溯都是没有返回值的,这题的res是全局遍量,所以也不需要return
                      参数的话我们需要一个startIndex来让下一次递归知道我们下一次是从那个index开始循环,然后一个二维数组用来记录结果,一个一维数组记录
                      经过的路径
                   2）什么时候返回：一般组合,切割,子集和皇后问题都是再叶子节点返回.这题是组合问题,那么就是当path的长度等于k的长度的时候 
                   3）每一层的回溯发生什么:这里递归的层数是根据k的值来定的,再每一层递归中我们记录路径,然后当回溯的层数小于k的值时继续下一层的递归,然后回溯
        """
        path, res,startIndex = [],[],0
        def backTracking(n,k,startIndex):
            nonlocal path,res
            if len(path)==k:
                res.append(path[:]) # 记住这里要用path的copy因为path是数组,它的值是一直在变得,不用copy的话append的值不是当前记录的值了
                return
            for i in range(startIndex,n):
                path.append(i)
                backTracking(n,k,i+1)
                path.pop()
        backTracking(n+1,k,1)
        return res