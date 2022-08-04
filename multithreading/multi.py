from threading import *
import time

def f1():
    for x in range(5):
        print(x)


t1 = Thread(target=f1, args=[5], name='thread1')

def f2():
    for x in range(6, 11):
        time.sleep(3)
        print(current_thread().name, x)


t2 = Thread(target=f2(), name='thread2')
t1.start()
t2.start()
t1.join()
t2.join()