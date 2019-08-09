import re

def main():
    sentence = 'You fucking idiot, shithole, dumbass, bitch, whatev.'
    # sub(pattern, repl, string, count=0, flags=0)
    # 用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数
    censor = re.sub('fuck|shit|ass|bitch','**',sentence,flags=re.IGNORECASE)
    print(censor)
    """ re模块的正则表达式相关函数中都有一个flags参数，
    它代表了正则表达式的匹配标记，可以通过该标记来指定匹配时是否忽略大小写、
    是否进行多行匹配、是否显示调试信息等。如果需要为flags参数指定多个值，
    可以使用按位或运算符进行叠加，如 flags = re.I | re.M"""

if __name__ == "__main__":
    main()