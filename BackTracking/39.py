#给定一个数组,数组里的元素可以重复去取.然后求数组里全部的组和,组合的和需要等于target
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
    
a = "mno"
print(a[:1])