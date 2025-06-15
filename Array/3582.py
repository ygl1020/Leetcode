#根据条件来生成title
def generateTag(self, caption: str) -> str:
        caption = caption.strip()
        if not caption:
            return "#"
        strings = caption.split()
        print(strings)
        strings[0] = strings[0].lower()
        for i in range(1,len(strings)):
            strings[i] = strings[i].capitalize()
        print(strings)
        res = "".join(strings)
        res = "#" + res
        if len(res)>100:
            return res[:100]
        else:
            return res