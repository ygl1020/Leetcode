def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    这里的去重是树层的去重,去重的原因是在之前的循环中已经记录了这个组合[1,2,2,5]在 1,2之后 可以有 2,2,5, 然后第一个2已经记录了 1,2,2这个组合,如果不树层去重,第2个2也会有1，2，2.
    另外这题我们需要用一个startIndex来保证下一层中开始取数的范围不会包括上一层已经被选取的值,所以我们需要把i+1传入backTracking里面
    """
    #method 1
    candidates.sort()
    startIndex,res,path = 0,[],[]
    
    def backTracking(startIndex,target):
        if sum(path) >= target:
            if sum(path) == target:
                res.append(path[:])
            return 
        for i in range(startIndex,len(candidates)):
            if i >startIndex and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            backTracking(i+1,target)
            path.pop()
    backTracking(0,target)
    return res

    """
    这题其实有一点抽象,因为它说的去重是树层方向的去重而不是数值方向的去重。所以这题的话我们需要额外引入一个used参数再递归当中,然后每一个节点我们判断这个节点的值和之前那个节点的值是否是一样的并且它的上一个used的值是否为FALSE,如果条件满足,那么我们就跳过当前节点.
    
    """
    #method2
    res, path,used = [],[], [False] * len(candidates)
    candidates.sort()
    def backTracking(candidates,target,startIndex,total,used):
        if total >= target:
            if total >target:
                return
            if total == target:
                res.append(path[:])
                return 
        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i-1] and not used[i - 1]:
                continue
            # if total + candidates[i] > target:
            #     break
            total += candidates[i]
            used[i] = True
            path.append(candidates[i])
            backTracking(candidates,target,i+1,total,used)
            used[i] = False
            total -= candidates[i]
            path.pop()
        return res
    backTracking(candidates,target,0,0,used)
    return res