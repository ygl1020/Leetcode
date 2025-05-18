#给你一个字符串,然后让你判断字符串里面的括号是否都是完整的
def isValid(self, s: str) -> bool:
        """
        for循环遍历字符串,遇见左括号把对应的右括号入栈.这个for循环的过程中,如果左括号不匹配右括号-->1)左右括号不符合 stack[-1]!= i, 2)右括号多于左括号 stack 是空的 那么我们就直接return fasle 3）最后如果左括号
        多于右括号,for 循环结束stack不为空,也返回false
        """
        if len(s) %2 !=0:
            return False
        res = False
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or i != stack[-1]: # 当左括号少于右括号时,stack里面的element会出现空值,这时如果运行stack[-1]会报错,另外如果当前的值不等于stack[-1],也是错的
                return False
            else:
                stack.pop() 

        return False if stack else True #处理左括号多余右括号时的情况