"""
In Thread_Communicaton_Incorrect.py, each of 100 threads sent $1 
to the account, yet in the end the account balance is $1. Why? 

The reason is that the multi threads would run the code 
            new_balance = self._balance+money
at the same time, and at that moment, all of the threads 
have an initial account balance of $0, and thus all of them
run new_balance = $0 + $1. As a result, the output is $1. 

In this case, we need to use "lock" to protect such resources. 
Only threads with the "lock" are allowed to run on the resources, 
i.e. in this program, the account balance. Others, without the lock. 
have to be jammed and wait for the current thread releases the lock 
and pass the lock to the next thread. 
"""

from time import sleep
from threading import Thread, Lock 

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self,money):
        # First the thread need to acquire a lock
        self._lock.acquire()
        try:
            new_balance = self._balance+money
            sleep(0.1)
            self._balance = new_balance
        finally:
        # No matter if there is an exception or not, 
        # thread needs to release the lock
            self._lock.release()

    @property 
    def balance(self):
        return self._balance

class AddMoney(Thread):
    def __init__(self,account,money):
        super().__init__()
        self._account = account 
        self._money = money 

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoney(account,1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('Account Balance: $ %d' % account.balance)

if __name__ == "__main__":
    main()