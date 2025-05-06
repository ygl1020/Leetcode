"""
这题需要把字符串进行反转,解题的思路是先把前后的空格去除,
然后把s按照空格进行分割,最后用双指针来进行反转.这里要用strip()和split()函数,
一开始我用的split(" ")是错误的,因为这样的话只会对空格的情况进行分割,但是如果遇到tab或者其他空格的形式就不管用了.
"""
def reverseWords(self, s: str) -> str:
        s = s.strip()
        tmp = s.split()
        left,right = 0,len(tmp)-1
        while left <right:
            tmp[left],tmp[right] = tmp[right],tmp[left]
            left +=1
            right-=1
        return " ".join(tmp)