#判断连续不重复的字符串的最长长度
def lengthOfLongestSubstring(self, s: str) -> int:
        """
        解法一暴力解，两个for循环,第一个for循环起到确定遍历窗口的作用,然后每次我们初始化一个set,第二个for循环我们遍历从第一个for循环开始一直到字符串结束的所有字符串
        查看是否有任意一个字符串出现再set里面,如果有的话就直接退出第二个for循环,如果没有更新set和res
        """
        # res = 0
        # for i in range(0,len(s)):
        #     charSet = set()
        #     for j in range(i,len(s)):
        #         if s[j] in charSet:
        #             break
        #         charSet.add(s[j])
        #         res = max(res,j-i+1)
        # return res

        # sliding windows
        """
        我们初始化一个空的set来保存unique element,l指针和res来记录最长的数组.然后我们遍历每一个元素,在for循环中,我们需要用一个while循环来判断s[r]的元素是否在unique里面.然后再
        的话我们要不断删除s[l]所代表的值同时更新l指针一直到s[r]不再unique里面,这样做的原因是-->'pkkw',再r等于2时,set里面有p,k由于我们要求连续子字符串的最长长度,所以我们要删除
        p和k,那么p就是s[l], k就是s[l+1],然后这时while循环结束,我们把第s[r]放入unique,更新res并继续for循环
        """
        unique = set()
        l = 0
        res =0
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            res = max(res,r-l+1)
        return res
        # method 3
        unique  = set()
        l,r = 0,0
        res = 0
        for r in range(0,len(s)):
            if s[r] not in unique:
                unique.add(s[r])
                res = max(res, r-l+1)
            else:
                while s[l] != s[r]:
                    unique.remove(s[l]) # 因为我们需要找连续的最长不重复字符串,所以当遇见重复的字符串时，我们需要移动左指针,一直到我们找到和当前s[r]相同的字符串.这个过程中我们需要不断删除s[r]在unique里面的value
                    l+=1
                l+=1
                unique.add(s[r])
                print(l,r)
        return res