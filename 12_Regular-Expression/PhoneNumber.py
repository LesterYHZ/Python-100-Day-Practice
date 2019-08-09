"""
Given: A sentence in which there can be regular numbers or specific 
phone numbers

Find: Use RE to find the phone numbers

电信: 133/153/180/181/189/177
联通: 130/131/132/155/156/185/186/145/176
移动: 134/135/136/137/138/139/150/151/152/157/158/159/182/183
      184/187/188/147/178
"""

import re

def main():
    # compile(pattern)
    # 编译正则表达式返回正则表达式对象
    pattern = re.compile(r'(?<=\D)1[345780]\d{9}(?=\D)') 
    """
    (?<=exp)        匹配exp后面的位置
    \D              匹配非数字
    (?=exp)         匹配exp前面的位置
    """
    sentence = '''Dva\'s MEKA number is 8462512326548456;
         her phone number is 13802451956; remember,
              it\'s not 15640255832; phone numbers include
                   110, 911, 120, etc. My phone number is 13080861622. '''
    # findall(pattern, string)
    # 查找字符串所有与正则表达式匹配的模式 返回字符串的列表
    mylist = re.findall(pattern,sentence)
    print(mylist)
    print('---------ˋ( ° ▽、° ) ---------')
    # finditer(pattern, string)
    # 查找字符串所有与正则表达式匹配的模式 返回一个迭代器
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('---------ˋ( ° ▽、° ) ---------')
    # search(pattern, string)
    # 搜索字符串中第一次出现正则表达式的模式 成功返回匹配对象 否则返回None
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())
    print('---------ˋ( ° ▽、° ) ---------')
    """Better Pattern"""
    pattern = re.compile(r'(?<=\D)(13[0-24-9]\d{8}|1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)') 
    mylist = re.findall(pattern,sentence)
    print(mylist)

if __name__ == "__main__":
    main()