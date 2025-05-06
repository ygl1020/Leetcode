def reverseString(self, s: List[str]) -> None:
        """
        这题是非常典型的双指针的写法,设置left,right指针,然后开始while循环
        """
        left,right = 0,len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1
        return s