import json
import re

class HiddenChars():
    def __init__(self, filename):
        emojisFd = open(filename, "r", encoding="utf-8")
        emojisJson = json.loads(emojisFd.read())
        emojisFd.close()
        # Start with replacing higher width emojis
        self.emojiJson = sorted(emojisJson, key=lambda x: x["width"], reverse=True)
        self.revealSymbol = '☒'
        self.regex = re.compile(r'[\w\d\._-]',  re.UNICODE)
    
    def getReveal(self, input):
        tmp = input
        tmp = self.regex.sub('0', tmp)
        result = ""

        for emoji in self.emojiJson:
            tmp = tmp.replace(emoji["name"], "0"*emoji["width"])
        
        for i in range(len(tmp)):
            if tmp[i] != "0":
                result += self.revealSymbol
            else:
                result += input[i]

        return result