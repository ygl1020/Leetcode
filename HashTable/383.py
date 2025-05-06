"""
这题需要求是否magazine里面出现的元素涵盖ransomNote里面所有出现的元素. 这题的思路是先把magazine里面的元素遍历一遍放入一个dict,key为元素本身,value为出现的次数
之后我们遍历ransomNote然后看当前元素是否在dict里面如果在的话它的value是否大于0,否者的话就返回false

"""
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        for i in magazine:
            if i not in magazine_dict:
                magazine_dict[i] =1
            else:
                magazine_dict[i] +=1
        for j in ransomNote:
            if j not in magazine_dict:
                return False
            else:
                if magazine_dict[j] >0:
                    magazine_dict[j] -=1
                else:
                    return False
        return True