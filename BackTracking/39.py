#给定一个unique数组,数组里的元素可以重复去取.然后求数组里全部的组和,组合的和需要等于target
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    回溯中backtracking里面放入的startindex是用了控制下一层的取值范围,比如题目说不可以重复取值,那么值取完index0之后下一层需要从index1开始取,因此是i+1,
        如果题目不要求一个index只可以取一次,那么我们就可以直接把i传入backtracking函数.这里说了array里面的值都是unique的,所以我们不需要考虑层级去重的
        层级去重会出现的情况是当array里面没有说都是unique元素,那么如果index2和index3的值都是相同的,那么在同一层中先计算index2的组合,之后计算index3的组合就会出现和index2组合相同的答案
        因此我们需要进行去重
    
    """
    #method1
    res,path,startIndex = [],[],0
    def backTracking(startIndex):
        if sum(path) >= target:
            if sum(path) == target:
                res.append(path[:])
            return
        for i in range(startIndex,len(candidates)):
            path.append(candidates[i])
            backTracking(i)
            path.pop()
    backTracking(startIndex)
    return res
    #method 2
    if not candidates:
        return []
    path,res,startIndex,total = [],[],0,0
    def backtracking(candidates,target,startIndex):
        nonlocal total
        if total == target:
            res.append(path[:])
        if total > target:
            return
        for i in range(startIndex,len(candidates)):
            if i>startIndex and candidates[i] ==candidates[i-1]: # 因为是层序遍历,for循环里面的逻辑是那一层的逻辑,所以我们把去重逻辑放在这里 另外i > startIndex 的原因是为了防止范围溢出
                continue
            total += candidates[i]
            path.append(candidates[i])
            backtracking(candidates,target,i) #这里的statindex是i因为我们往下的一个回合还是可以重复取值,所以我们希望从当前的i开始进行遍历
            total -= candidates[i]
            path.pop()
    backtracking(candidates,target,startIndex)
    return res

