#根据digits里面的映射string来求组合的所有可能性
def letterCombinations(self, digits: str) -> List[str]:
        """
        这题我一开始的思路是用两层for循环来回溯,但是这样其实是错误的,我们只需要用一层for循环,for循环的层数是根据len(digits)来定的,即如果"23"那就有
        两层for循环,循环的宽度是由digits里面的数字对应的字符串长度来订的.因此再每一层的for循环中,我们只需要再在当前digits[index]--->2:abc, 里面
        循环就可以了. 这题我们需要一个index用来记录我们走到digits里面的哪一个值了。注意这里的index和77的startIndex不一样.77的startIndex是在一个集合里面
        求组合,因此我们需要记录我们在这个集合里面走到了哪里,这里的index值的是digits string里面我们走到了哪里
        
        这题的话也要有一个startIndex,但是这题的startindex不是用来记录一个数组遍历到哪里了,而是用用来记录digits里面我们走到了哪里.另外就是这题返回的是一维数组所以我们不需要用path数组来存放结果
        直接用一个string来把结果借助就可以了.之后有一个小技巧用来回溯字符串需要记住
        """
        if not digits:
            return []
        ref = {
            "0":"",
            "1":"",
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        string = ""
        def backTracking(digits,index):
            nonlocal res, string
            if len(string) ==len(digits):
                res.append(string) # 因为是string所有不需要用深拷贝
                return
            digit = digits[index]
            for number in ref[digit]:
                string +=number
                backTracking(digits,index+1)
                string= string[:-1]  # 记住字符串的回溯技巧
        backTracking(digits,0)
        return res
a = "mno"
print(a[:-1])