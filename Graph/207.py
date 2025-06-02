# 判断class是否可以选取成功
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        解题思路是先构建一个字典,字典的key是class,value是它的preReq, 然后我们需要一个visited元组用来存储当前dfs中遍历过的class.解题的逻辑为判断dfs的过程中是否存在circle, circle的判断是通过
        当前cla是否在visited中出现过来判断的. dfs函数中的逻辑是如果出现了环-->if cla in visited 我们直接return false, 如果classPre[cla]为空列表-->没有preReq 我们直接return True
        否者的话我们把当前cla放入visited元组,然后开始通过dfs遍历当前cla的全部classPes, 如果其中一个return false,那么就代表有环,否者的话我们去除graph中这个cla的全部edge并且在visited移除cla
        ---->visited.remove(cla)和classPre[cla] = [].  这两个步骤很关键1)当我们确定这个calss可以成功选取,我们就需要可以直接把这个class的preClass清空,方便后面的计算 2)如果不在visited把这个
        cla移除那么可能后面的某个cla会有preClass为当前的这个cla,应该判断cla in visited 出错就会return False.
        最后我们还需要一个for循环来遍历全部的class,只有每一个cla都可以成功选取,我们才可以return True,原因是如果出现的disconnected classs preReq,只判断一个class的dfs结果就会出错eg: 
        n=4, [[0,1], [3,2],[2,3]], 这里如果判断完0，1 class然后不继续判断2，3就会出现错误的情况,因为后面的2，3有环
        """
        classPre = {cla:[] for cla in range(numCourses)}
        for cla,pre in prerequisites:
            classPre[cla].append(pre)
        visited = set()
        # print(classPre)
        def dfs(cla):
            if cla in visited:
                return False
            if not classPre[cla] :
                return True
            visited.add(cla)
            for pre in classPre[cla]:
                if not dfs(pre):
                    return False
            visited.remove(cla)
            classPre[cla] = []
            return True
        for cla in range(numCourses):
            if not dfs(cla):
                return False
        return True