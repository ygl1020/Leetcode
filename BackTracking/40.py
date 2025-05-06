def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    这题其实有一点抽象,因为它说的去重是树层方向的去重而不是数值方向的去重。所以这题的话我们需要额外引入一个used参数再递归当中,然后每一个节点我们判断这个节点的值和之前那个节点的值是否是一样的并且它的上一个used的值是否为FALSE,如果条件满足,那么我们就跳过当前节点.
    
    """
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