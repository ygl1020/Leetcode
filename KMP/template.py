#查找一个字符串是否再另一个字符串中出现的问题匹配的问题 leetcode28
class Solution:
    """
    kpm的思路创建一个模式串的前缀表,这个表是一个长为len(模式串),每一个index代表的value是以当前index及index之前的字符串的最长相等前后缀的值.
    根据这个表我们再主串中进行遍历时如果出现不匹配的情况,我们退回到next(i-1)--前缀表--的位置继续进行比较,这样的话就可以效率最大化的利用已经对比过的相同字符串
    
    这里getNext就是获取这个模式串前缀表的具体代码实现,具体情况分为4步 1)初始化 2)在模式串中把当前字符串[0,j]的index j和i的值进行比较 如果是不相等的情况 3)如果相等的情况 4)更新前缀表(next)
    1)初始化: j 代表的是当前模式串[0:j]的前缀的最后一个index 以及当前index以及之前的模式串的最长前后缀的相等长度,前缀可以为0所以我们起始化为0.  next前缀表array的第一个数值--> next[0] =0,因为长度为1的模式串没有前后缀
    2) i代表是当前模式串[0:j]的后缀的最后一个index, 因为要和前缀的最后一个index i作比较所以需要从1开始 这个很重要
       另外处理 s[i] != s[j]的情况, 当s[i] != s[j]时,我们把j移动到j在next的下标的前一个index,所以需要用while循环. 另外我们要注意j不可以等于0,所以要加一个j>0的条件
    3) 当s[i] == s[j]的情况,我们把j增加1
    4) 更新next前缀表: 注意我们更新的index为next[i]的位置,值为j
    
    之后的话我们可以调用getNext函数,因为我们是直接修改的next array所以不需要再getNext函数中进行return
    还是相同的步骤,1)初始化,2)再主串中进行遍历,这里要特别注意我们是从index 0开始而不是1了,因为再创建前缀表的时候我们再getNext函数中的for循环是从index 1开始的
    因为strStr里面的i代表的是haystack主串的index j代表的是模式串的index和getNext函数里面的i,j的含义是不一样的
    当主串的[i]!=模式串的[j]是-->while j >0 and haystack[i] != needle[j]: 我们根据前缀表来更新j的值
    3)当主串的[i]==模式串的[j]是-->while j >0 and haystack[i] == needle[j]: 我们把j的值+1
    4)这里因为for循环的范围是主串的长度,所以当我们发现j==模式串的长度时就返回--> if j == len(needle):return i-j+1
    5)如果循环结束再主串中没有发现模式串,那么就返回-1
    
    """
    def getNext(self,next,s):
        #initiate j and next, j represnets the index of last element of prefix of current string from [0:j]
        j =0
        next[0] = 0
        # generate prefix array of s
        for i in range(1,len(s)): #2
            # when s[i] != s[j], we go back the last index of j, iterational process so we need while loop
            while j>0 and s[i] != s[j]:
                j = next[j-1]
            # when s[i] ==s[j], increase j by 1
            if s[i] == s[j]:
                j +=1
            # update the prefix table at each end of iteration
            next[i] = j
            
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        next = [0] * len(needle)
        self.getNext(next,needle)
        for i in range(len(haystack)): #3
            while j >0 and haystack[i] != needle[j]:
                j = next[j-1] #1
            if haystack[i] == needle[j]:
                j +=1
            if j == len(needle):
                return i-j+1
        return -1