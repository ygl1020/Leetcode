# 计算后置运算

def evalRPN(self, tokens: List[str]) -> int:
    """
    这题也是根据stack来解,需要理解这里的反转波兰表达式是后置运算的表达方式(如果写成二叉树的形式),但是平时我们习惯的是中置表达式,所以这里其实就是后置表达式的运算.具体的操作就是遇见num把他入栈,遇见operant就出栈两个数字
    进行计算,然后把这个结果入栈.需要注意加号和乘号的计算不需要考虑num1和num2的顺序,但是处理减和除的时候是要把num2放在前面. 另外题目要求取最大整除数并且到0为止,这个需要特别注意一下不能用//否则遇见负数的情况就变成-1了-->违反规则
    然后第一种写法是我自己写出来的,但是超时了,需要优化为第二种写法: 把if elif拆分成if, else,这样的不需要每次都把全部情况过一遍,当我们知道i是数字时一种情况,是运行符时是一种情况
    第三种写法:延续第二种写法的优化,把num1和num2的出栈提取出来放在else的开头, 然后去除中间值零时值的命名
    
    """
    #method 1
    stack = []
    for i in tokens:
        if i not in "+-*/":
            stack.append(int(i))
        elif i == "+":
            num1 = stack.pop()
            num2 = stack.pop()
            tmp = num2 + num1
            stack.append(tmp)
        elif i == "-":
            num1 = stack.pop()
            num2 = stack.pop()
            tmp = num2 - num1
            stack.append(tmp)
        elif i == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            tmp = num2 * num1
            stack.append(tmp)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            tmp = int(num2 / num1) #用num2//num1是取最大整除数,但是如果是(6 / -132) 会返回-1,但是题目要求truncate to 0,所以可以用int(num2/num1)
            stack.append(tmp)
    return int(stack.pop())

    #method 2:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                if i == "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    tmp = num2 + num1
                    stack.append(tmp)
                elif i == "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    tmp = num2 - num1
                    stack.append(tmp)
                elif i == "*":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    tmp = num2 * num1
                    stack.append(tmp)
                else:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    tmp = int(num2 / num1) #用num2//num1是取最大整除数,但是如果是(6 / -132) 会返回-1,但是题目要求truncate to 0,所以可以用int(num2/num1)
                    stack.append(tmp)
        return int(stack.pop())
    #method 3
    stack = []
    for token in tokens:
        if token not in {"+", "-", "*", "/"}:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # Truncate towards zero
    return stack.pop()