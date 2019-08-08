"""
JSON means JavaScript Object Notation

JSON                Python
-------------------------------
object              dict
array               list
string              str
number(int/real)    int/float
true/false          True/False
null                None
"""

import json

def main():
    mydict = {
        'name': 'Hana Song',
        'age': 19,
        'email': 'Dva.overwatch.com',
        'WeChat': 16548484651510,
        'friends': ['Mercy','Tracer'],
        'vehicles':[
            {'brand':'MEKA','max_speed':200},
            {'brand':'FURY','max_speed':265},
            {'brand':'GEGURI','max_speed':254}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
    except IOError as e:
        print(e)
    print('THE END')

"""
Four important json functions:
dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象
"""

if __name__ == "__main__":
    main()