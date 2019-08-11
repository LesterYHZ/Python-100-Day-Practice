"""
Consider the following codes:

from random import randint
from time import time, sleep

def download(filename):
    print('Downloading %s...' % filename)
    time_download = randint(5,10)
    sleep(time_download)
    print('Done! Downloading took %.2f sec' % time_download)

def main():
    start = time()
    download('Dead or Alive.webm')
    download('Lara in Trouble.avi')
    end = time()
    print('Done! Downloading took %f sec' % (end-start))

if __name__ == '__main__':
    main()

The output on screen should be:

Downloading Dead or Alive.webm...
Done! Downloading took 10.00 sec
Downloading Lara in Trouble.avi...
Done! Downloading took 6.00 sec
Done! Downloading took 16.000854 sec

which means that these two download() run seperately and only after
the first download() is down can the second began

We can therefore use multiprocessing to make the two download() run 
at the same time
"""

from multiprocessing import Process
from os import getpid 
from random import randint 
from time import time, sleep 

def download(filename):
    print('Download process [%d] started.' % getpid())
    print('Start downloading %s...' % filename)
    time_download = randint(5,10)
    sleep(time_download)
    print('Done downloading %s, taking %d sec. ' % (filename,time_download))

def main():
    start = time()
    p1 = Process(target = download, args = ('Dead or Alive.webm',))
    p1.start()
    p2 = Process(target = download, args = ('Lara in Trouble.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('Done downloading, taking %.2f sec in total. ' % (end-start))

if __name__ == "__main__":
    main()

""" The output is: 
Download process [14168] started.
Start downloading Dead or Alive.webm...
Download process [2348] started.
Start downloading Lara in Trouble.avi...
Done downloading Lara in Trouble.avi, taking 8 sec.
Done downloading Dead or Alive.webm, taking 9 sec.
Done downloading, taking 9.16 sec in total.
"""