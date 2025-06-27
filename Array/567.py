#给定两个str 让你判断s2中有没有s1的permutation
def checkInclusion(self, s1: str, s2: str) -> bool:
    """
    遍历一遍s1来创建一个hash table,然后用左右指针来固定一个窗口的长度,不断移动这个窗口.再窗口里判断当前的sequence的element是否和s1的是一样的
    """
    if len(s2) < len(s1):
        return False
    counts = {}
    for s in s1:
        counts[s] = counts.get(s,0) +1
    copy = counts.copy() 
    total = len(s1)
    l,r =0,len(s1)-1
    while r<len(s2):
        for i in range(l,r+1):
            if s2[i] not in copy:
                copy = counts.copy()
                total = len(s1)
                l +=1
                break
            copy[s2[i]]-=1
            total -=1
            if copy[s2[i]] <0:
                copy = counts.copy()
                l +=1
                total = len(s1)
                break
            if total ==0:
                print("res",copy,s2[i])
                return True
        r+=1
    return False