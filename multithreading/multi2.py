from threading import Thread
def f1(n):
    for x in range(n):
        print(x)
t1 = Thread(target=f1,args=[5])
t1.start()