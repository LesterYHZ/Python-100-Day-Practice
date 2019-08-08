"""
class 'bytes'
copy and paste a picture
"""

def main():
    try:
        with open('dva.jpg','rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('baby-dva.jpg','wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('Can\'t open the file')
    except IOError as e:
        print('Error in reading and writing')
    print('The End')

if __name__ == "__main__":
    main()