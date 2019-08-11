"""
Same program as that in MultiProcessing.py but used multi threads
"""

from random import randint
from threading import Thread
from time import time, sleep 

def download(filename):
    print('Start downloading %s...' % filename)
    time_download = randint(5,10)
    sleep(time_download)
    print('Done downloading %s, taking %d sec. ' % (filename,time_download))

def main():
    start = time()
    p1 = Thread(target = download, args = ('Dead or Alive.webm',))
    p1.start()
    p2 = Thread(target = download, args = ('Lara in Trouble.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Done downloading, taking %.2f sec in total. ' % (end-start))

if __name__ == "__main__":
    main()

""" Output: 
Start downloading Dead or Alive.webm...
Start downloading Lara in Trouble.avi...
Done downloading Lara in Trouble.avi, taking 5 sec.
Done downloading Dead or Alive.webm, taking 10 sec.
Done downloading, taking 10.00 sec in total.
"""