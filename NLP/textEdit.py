import re

def lengthFilter(sentence):
    return [item for item in sentence if (len(item)>3 and len(item)<50)]

def readText(path):
    with open(path, encoding='utf-8') as f:
        line = f.read()
    line=line.replace("\n","")

    return line

#进一步对一些特殊的字符进行切割
def splitText(str):
    sentence=re.split('•', str)
    sentence=list(set(sentence))#防止出现重复语句
    # sentence=lengthFilter(sentence)
    return sentence