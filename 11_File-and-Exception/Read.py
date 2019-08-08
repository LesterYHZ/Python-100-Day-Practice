"""
'r'     read (default)
'w'     write (renew the texts)
'x'     write, if file already exists then exception
'a'     write after the existed file
'b'     10010011
't'     text (default)
'+'     renew (read and write)
"""

import time

def main():
    f = open('Dian-Jiang-Chun.txt','r',encoding='utf-8')
    print(f.read())
    f.close()

    """ If the open(file) doesn't exist, then there would be an error; 
    so we want to use Python's exception"""
    f = None
    try:
        f = open('Dian-Jiang-Chen.txt','r',encoding='utf=8') # File not exist
        print(f.read())
    # Use except to deal with various possible errors
    except FileNotFoundError:
        print('Can\'t open the file')
    except LookupError:
        print('Unknown code')
    except UnicodeDecodeError:
        print('Error in decoding')
    # Even if there are plenty of errors, the code under finally would run
    finally:
        if f:
            f.close()
    print()
    
    """Other than use read to read file, we can also use for-in
    or realines to read the file line by line and save them into a list"""
    # for-in
    with open('Dian-Jiang-Chun.txt',mode='r',encoding='utf-8') as f:
        for line in f:
            print(line,end='')
            time.sleep(0.5)
    print()
    # readlines
    with open('Dian-Jiang-Chun.txt',encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

if __name__ == "__main__":
    main()