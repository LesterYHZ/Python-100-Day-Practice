"""
Given   1~10000000
Find    Sum(1~10000000)

Don't you dare using for loop
"""

from multiprocessing import Process, Queue 
from random import randint 

def task(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number 
    # Save the temporary result in the queue
    result_queue.put(total)

def main():
    processes = []
    number_list = [x for x in range(1,10000001)]
    result_queue = Queue()
    idx = 0 
    # Start 8 processes, divide the data into slices, and then compute
    for _ in range(8):
        p = Process(target = task, args = (number_list[idx:idx+1250000],\
            result_queue))
        idx += 1250000
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    total = 0
    # Take the result saved in queue out
    while not result_queue.empty():
        total += result_queue.get()
    print(total)

if __name__ == "__main__":
    main()

