# 判断anagram 
def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1 = {}
        dict2 ={}
        for i in range(0,len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] +=1
            if t[i] not in dict2:
                dict2[t[i]] = 1
            else:
                dict2[t[i]] +=1
        print(dict1,dict2)
        for k in dict1.keys():
            if k not in dict2.keys():
                return False
            if dict1[k] != dict2[k]:
                return False
        return True