# Program without Multithreading

##def display():
##    for i in range(5):
##        print("Python")
##def show():
##    for i in range(5):
##        print("Java")
##        
##display()
##show()

# Program With Multithreading

##import threading
##def disp():
##    for i in range(5):
##        print("Python")
##def show():
##    for i in range(5):
##        print("java")
##
##t1=threading.Thread(target=disp)
##t2=threading.Thread(target=show)
##t1.start()
##t2.start()


### Program using class Concept
##import time
##import threading
##class MyThread(threading.Thread):
##    def run(self):
##        for i in range(5):
##            print("child")
##            time.sleep(2)
##t = MyThread()
##t.start()
##
##for i in range(5):
##    print("Parent")


##import threading,time
##def disp():
##    for i in range(5):
##        print("Hello I am Child")
##        time.sleep(0.2)
##
##def show():
##    for i in range(5):
##        print("Hello I am dusra child")
##        time.sleep(0.2)
##
##t=time.time()
##disp()
##show()
##print("Total time taken",time.time()-t)

import threading,time
def disp():
    for i in range(5):
        time.sleep(0.2)

def show():
    for i in range(5):
        time.sleep(0.2)

t=time.time()
t1 = threading.Thread(target=disp)
t2=threading.Thread(target=show)

t1.start()
t2.start()
print(t1.getName())#thread-1(By default)
print(t2.getName())#thread-2
t1.setName("First Thread")
t2.setName("Second Thread")

print(t1.getName())
print(t2.getName())
print(threading.active_count())
print(threading.enumerate())
