import time
import threading
from random import randint

global thread_var

answer = ""

locker = threading.Lock()

def thread_func(i):
    sleep_time = randint(0, 6)
    time.sleep(sleep_time)
    locker.acquire()
    try:
        print("Sleep for {0} seconds".format(sleep_time))
        thread_var = randint(0, 10)
        print("The mutex value is {0}".format(thread_var))
    finally:
        locker.release()


if __name__ == "__main__":

    while answer != "n":
        start_time = time.time()
        threadz = []
        for i in range(1, 6):
            thr = threading.Thread(target=thread_func, args = (i,))
            thr.start()
            threadz.append(thr)


        for thread in threadz:
            thread.join()

        print("The time of programm is {0} seconds ".format(time.time() - start_time))
        answer = str(raw_input("contunue? "))

