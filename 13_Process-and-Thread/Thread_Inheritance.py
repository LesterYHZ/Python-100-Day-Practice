"""
We can create our own thread class by inheriting the Thread class
"""

from random import randint
from threading import Thread
from time import time, sleep 

class Download(Thread):
    def __init__(self,filename):
        super().__init__()
        self._filename = filename 

    def run(self):
        print('Start downloading %s... ' % self._filename)
        time_download = randint(5,10)
        sleep(time_download)
        print('Downloading %s completed; took %d sec. ' % (self._filename,time_download))

def main():
    start = time()
    t1 = Download('Dead or Alive.webm')
    t1.start()
    t2 = Download('Lara in Trouble.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('In total took %.2f sec. ' % (end-start)) 

if __name__ == "__main__":
    main()