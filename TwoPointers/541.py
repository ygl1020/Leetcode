"""
这题需要把有以k为单位,再k的长度范围之内的char进行反转,然后后面按照2k的长度一直到len(s), 这里需要注意string是不可以做text[left],text[right] = text[right],text[left]操作的,如果我们要这样的话需要把s转化为list
第一个方法双指针的方法,起始p为0,然后当p<len(s)是while循环,循环里面我们用字符串slicing的方式处理字符串 1)定义需要reverse的字符串区间 2)进行字符串反转,这里需要注意这个公式是怎么来的 特别是别忘了s[:p]的存在 3)把p指针移动2k个单位
第二个方法的话是更传统的双指针的写法1)定义一个双指针函数,这里注意input类型为list 2)用for循环每次移动2k个单位,每一次循环我们处理一次需要进行反转操作的list 区间,注意这个是怎么做到的res[i:i+k] = reversing(res[i:i+k])
3)最后返回需要str类型,所以我们可以用''.join(res)来对string进行拼接

"""

def reverseStr(self, s: str, k: int) -> str:
        #method 1
        # p = 0
        # while p <len(s):
        #     p2 = p+k
        #     s = s[:p] +s[p:p2][::-1] +s[p2:]
        #     p = p+2*k
        # return s

        #method 2
        def reversing(text:list):
            left,right = 0,len(text)-1
            while left <right:
                text[left],text[right] = text[right],text[left]
                left+=1
                right-=1
            return text
        res = list(s)

        for i in range(0,len(s),2*k):
            res[i:i+k] = reversing(res[i:i+k])
        return ''.join(res)