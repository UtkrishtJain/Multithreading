from threading import*
import time

def f1(n):
    for x in range(n):
        time.sleep(4)
        print(current_thread().name,x)
start = time.time()
t1 = Thread(target=f1, args=[5], name='thread1')

def f2():
    for x in range(6,11):
        time.sleep(3)
        print(current_thread().name,x)
t2 = Thread(target=f2, name ='thread2')
def f3():
    while True:
        print('hello')
        