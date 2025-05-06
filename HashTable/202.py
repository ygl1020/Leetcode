def isHappy(self, n: int) -> bool:
    """
    这题的关键时看出题目要干什么,这里的话可以理解为把n里面的每一位数进行拆解取平方,然后一直进行下午,如果这个过程中出现重复的值那么就不是快乐数,否者拆解到1那么就返回为快乐数
    因此一开始的时候设计一个集合用来储存出现过的拆解,当n的值不为1时我们重复循环 并且在这个过程中持续的拆解n,如果拆解完的n在集合里面就返回false否者把拆解值进行更新并放入合集
    """
    seen = set()
    while n !=1:
        total = sum([int(num) **2 for num in str(n)])
        print(total)
        if total in seen:
            return False
        seen.add(total)
        n = total
    return True