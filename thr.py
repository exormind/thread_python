import time
import threading
from random import randint

cycle = True
thread_var = 0
locker = threading.Lock()

def thread_func(i):
    sleep_time = randint(0, 6)
    time.sleep(sleep_time)
    locker.acquire()
    try:
        print "Thread #", i
        print "Sleep for", sleep_time , "seconds"
        global thread_var 
        thread_var = randint(0, 10)
        print "The mutex value is", thread_var
    finally:
        locker.release()


def main_func(thread_count):
    start_time = time.time()
    threadz = []
    for i in range(0, thread_count):
        thr = threading.Thread(target=thread_func, args = (i,))
        thr.start()
        threadz.append(thr)


    for thread in threadz:
        thread.join()

    print "The final mutex value is", thread_var
    print "The time of programm is", time.time() - start_time, " seconds"

while cycle:
    
    threads = int(raw_input("Thread count? "))
    main_func(threads)
    answer = str(raw_input("Contunue? "))
    if answer == "n":
        main_func(threads)
        cycle = False

