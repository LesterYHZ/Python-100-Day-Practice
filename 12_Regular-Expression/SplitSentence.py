import re

def main():
    f = open('Dian-Jiang-Chun.txt','r',encoding='utf-8')
    poem = f.read()
    sentences = re.split(r'[,.，。\n ]',poem)
    # ['蹴罢秋千', '起来慵整纤纤手', '', '露浓花瘦', '薄汗轻衣透', '',
    #  '见客入来', '袜刬金钗溜', '和羞走', '', '倚门回首', 
    # '却把青梅嗅', '', '', '']
    while '' in sentences:
        sentences.remove('')
    for st in sentences:
        print(st)
    f.close()

if __name__ == "__main__":
    main()