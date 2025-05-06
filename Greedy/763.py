#给你一个字符串然后让你尽可能的分割不同的字串.字串的要求是里面的每一个element只能再当前字串中出现
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        需要把一个字符串切割成尽量多份,每一份字符串里面出现的元素只会再当前字符串中出现.那么我们就需要一个字典来记录每一个字符串的最后的index.先起始化size,end和res.他们
        分别代表当前字符串的长度,当前字符串的最后的位置以及最后的return结果数组. 然后我们开始遍历字符串,每次进入循环size+=1, 然后我们对比last_idx[s[i]] 和 end,如果last_idx[s[i]]大
        那么就更新end--->当前元素的最后一个index大于现在的end,为了满足切割条件需要更新end.当i==end时我们就知道当前字符串可以被切割,因此我们把当前字符串放入res,然后size更新为0并继续循环
        
        """
        last_idx = {}
        for i,v in enumerate(s): # map the unique key inside s and use the last index of key as value
            last_idx[v] = i
        print(last_idx)
        size,end,res=0,0,[]
        for i in range(0,len(s)): # traver over s,
            size+=1 # each iteratin, size increase 1
            if last_idx[s[i]] > end: # when the last idx of current element is bigger than current end, we need to update it
                end = last_idx[s[i]]
            if i == end: # if i ==end, then we know current substring is ready to be partitioned, we collect it and update size back to 0 then start next iteration
                res.append(size)
                size=0
        return res