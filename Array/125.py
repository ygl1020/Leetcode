#让你删除非数字以及大小写字母的字符串后判断是否是alindrome
def isPalindrome(self, s: str) -> bool:
        """
        这里需要注意的时non-alphanumeric代表我们只保留0-9以及大写和小写的26的字母,然后chars最好用[]别用""这样time complexicy好一些
        """
        chars  = []
        for i in s:
            if i.isalnum():
                chars .append(i.lower())
        clean_str = "".join(chars)
        print(clean_str)
        l,r = 0, len(clean_str)-1
        while l<=r:
            if clean_str[l] != clean_str[r]:
                return False
            l+=1
            r-=1
        return True