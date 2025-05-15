#在一个数组中把每一个anagram进行组合,最后返回一个二维数组
from collections import defaultdict
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        defaultdict(list)可以把任意一个缺失的key的value初始化为一个数组,这样就不会出现需要额外拍段.eg:res['a'].append(1)  # No KeyError, automatically creates res['a'] = []
        然后我们遍历strs数组里面的每一个元素,把每一个element进行排序,这样可以确保每一个Anagrams的变种都会被放入字典中
        最后return 字典的values,并且把他们放入一个数组
        """
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())