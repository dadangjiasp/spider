import threading
import time
 
class myThread (threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.delay)
        print ("Exiting " + self.name)
        
def print_time(threadName, delay):
    counter = 0
    while counter < 3:
        time.sleep(delay)
        print (threadName, time.ctime())
        counter += 1
        
threads = []

thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)
 

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)
 

for t in threads:
    t.join()
    
print ("Exiting Main Thread")