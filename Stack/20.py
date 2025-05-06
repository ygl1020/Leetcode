#判断字符串中的括号是否符合规定

def isValid(self, s: str) -> bool:
        """
        这题的思路当遇见左括号我们就放入对应的右括号进入stack里面,然后遇见右括号就开始出stack并进行匹配.那么这样的话我们有哪几种错误的情况呢1)当左括号多余右括号:这时我们遍历完s后stack不为空 2）当遇见右括号,我们出stack时发现出栈的元素和当前的item不匹配 
        3）当遇见右括号我们尝试出stack但是发现stack已经为none时.这样我们就总结出了三种错误的情况.因为情况三二是可以统一讨论的所以我们放在一个elif里面一起进行讨论,并且要注意把情况三先进行讨论因为如果stack为空那么就出不了栈了.
        其他情况的话就是当前的item匹配出栈的元素,我们直接出栈就好了.
        循环完如果stack里面不为空那么就是第一种错误.
        
        """
        if (len(s) %2) !=0:
            return False
        stack = []
        for item in s:
            if item =="(":
                stack.append(")")
            elif item=="[":
                stack.append("]")
            elif item=="{":
                stack.append("}")
            elif not stack or stack[-1] != item: # when encounter right 括号, first make sure stack is not null, this elif take care error 2 nad 3 case
                return False
            else: #when the 左括号 match 右括号时出栈
                stack.pop()
        if stack: # 最后循环结束如果stack还有元素就是error 1
            return False
        return True