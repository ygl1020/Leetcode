#写两个function来decod和encode字符串
def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
            我们把每一个字符串的长度放再起始位置,然后加一个分割符号来辅助后面decode时的切分
        """
        res = ''
        for s in strs:
            res += str(len(s)) + '#' +s
        return res
        

def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    我们再字符串中先找到分隔符,然后计算当前需要decode的字符串的长度,然后把字符串放入res数组,最后更新i的下标
    """
    res,i = [],0
    while i <len(s):
        j = i
        while s[j] != '#':
            j+=1
            print(j,len(s))
        # print(s[i:j])
        length = int(s[i:j])
        res.append(s[j+1:j+1+length])
        i=j+1+length
    return res     