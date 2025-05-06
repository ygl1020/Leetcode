#删除string里面相邻的char
def removeDuplicates(self, s: str) -> str:
        """
        这题的思路是用栈,遍历s,如果当前i和stack的最后一个元素相等就出栈，否者的话就入栈(当最后一个栈的最后一个元素不等于当前的i时)
        最后返回stack,把stack转化为list并转化为string
        """
        if not s: # if s is empty
            return None
        stack = []
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(list(stack))