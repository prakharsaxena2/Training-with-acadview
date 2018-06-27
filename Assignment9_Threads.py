import threading        #Q.1
'''threading module inmported'''
import time
'''time module imported'''

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self , name):
        threading.Thread.__init__(self)
        self.name = name
    '''Method to Initialize myThread class'''

    def run(self):
        print("Starting" + self.name)
        print_time(self.name, 10 , 5)
        print("Exiting" + self.name)
    '''Method to Run the thread'''

def print_time(threadName , counter , delay):
    while counter :
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s running: %s" % (threadName , time.ctime(time.time())))
        counter -= 1
'''Method to print the Thread Statement'''

thread1 = myThread("Thread-1")
'''Creating new Thread'''
thread1.start()
'''Starting new Thread'''


import threading        #Q.2
'''threading module inmported'''
import time
'''time module imported'''

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self , name):
        threading.Thread.__init__(self)
        self.name = name
    '''Method to Initialize myThread class'''

    def run(self):
        print("Starting" + self.name)
        print_time(self.name, 10 , 1)
        print("Exiting" + self.name)
    '''Method to Run the thread'''

def print_time(threadName , counter , delay):
    while counter :
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%d: %s" % ((11 - counter) , time.ctime(time.time())))
        counter -= 1
'''Method to print the Thread Statement'''

thread1 = myThread("Thread-1")
'''Creating new Thread'''
thread1.start()
'''Starting new Thread'''



import threading            #Q.3
'''threading module inmported'''
import time
'''time module imported'''

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self , name):
        threading.Thread.__init__(self)
        self.name = name
    '''Method to Initialize myThread class'''

    def run(self):
        print("Starting" + self.name)
        print_time(self.name , 2)
        print("Exiting" + self.name)
    '''Method to Run the thread'''

def print_time(threadName , delay):
    for i in range(0 , 5):
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % ((str(l[i])) , time.ctime(time.time())))
        delay += 2
'''Method to print the Thread Statement'''

l = ["Element1" , "Element2" , "Element3" , "Element4" , "Element5"]
'''Creating List'''
thread1 = myThread("Thread-1")
'''Creating new Thread'''
thread1.start()


import threading            #Q.4
'''threading module inmported'''
import math
'''math module imported'''

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self , num):
        threading.Thread.__init__(self)
        self.num = num
    '''Method to Initialize myThread class'''

    def run(self):
        global result
        result = math.factorial(self.num)
        '''Calling factorial function'''
        print("%s: " % (self.name))
    '''Method to Run the thread'''

t = myThread(int(input("Enter the number to calculate factorial: ")))
'''Creating new Thread'''
t.start()
'''Starting new Thread'''
print("The factorial of %d is %d" % (t.num,result))
