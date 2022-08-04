from threading import*
def f1(n):
    for x in range(n):
        print(current_thread().name,x)
t1 = Thread(target=f1,args=[5], name='thread1')
t1.start()
print(current_thread().name)

def f2():
    for x in range(6,11):
        print(current_thread().name,x)
t2 = Thread(target=f2, name='thread2')
t2.start()
print(current_thread().name)