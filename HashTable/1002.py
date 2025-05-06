"""
这题要求找到在words里的每一个字符串中都出现过的char 然后char可以重复
具体的思路为先找到words[0]里面每一个char出现的次数,然后遍历words的每一个element找overlap,这里colletions.Counter的作用是返回一个dict然后key是每一个unique string, value是出现的次数
然后我们遍历所有words里面的元素找overlap,最后我们把这个更新后的tmp dict来过滤一遍,当里面的key所代表的value>0时我们就把这个key放入result array里面

这题不能用set因为set会把replicate排除,它只是找到unique value但是步记录这个value出现了多少次
"""

def commonChars(self, words: List[str]) -> List[str]:
        tmp = collections.Counter(words[0])
        print(tmp)
        result = []
        for i in range(1,len(words)):
            tmp = tmp & collections.Counter(words[i])
        print(tmp)
        for k,v in tmp.items():
            key,value = k,v
            print(key,value)
            while value>0:
                result.append(key)
                value -=1 
        return result
    
print(sum([2,3]))