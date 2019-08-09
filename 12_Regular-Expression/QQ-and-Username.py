"""
Input: QQ, Username
Output: Info about if QQ and Username are valid

Requirement: Username should consist of characters, numbers, and 
            underscore, with a length between 6 to 20 chars
            QQ should be 5~12 numbers and the first number can not
            be zero
"""

import re 

def main():
    username = input('Username: ')
    qq = input('QQ: ')
    # re.math(pattern, string)
    # 用正则表达式匹配字符串 成功返回匹配对象 否则返回None
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    """
    ^       匹配字符串的开始
    []      匹配来自字符集的任意单一字符
    {N}     匹配N次
    {M,}    匹配至少M次
    {M,N}   匹配至少M次至多N次
    $       匹配字符串的结束
    \d      匹配数字
    """
    if not m1:
        print('Username invalid')
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('QQ invalid')
    if m1 and m2:
        print('Valid info')

if __name__ == "__main__":
    main()