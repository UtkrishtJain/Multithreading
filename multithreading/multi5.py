from threading import*
class A(Thread):
    def run(self):
        for x in range(5):
            print(x)
ob=A()
ob.start()
class A():
    def run(self):
        for x in range(5):
            print(x)
ob=A()
t1=Thread(target=ob.run)
t1.start()