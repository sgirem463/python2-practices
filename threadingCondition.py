import threading
import time
import Queue

count = 0

def T1Processing():
    global count
    while True:
        cv.acquire()
        cv.wait()
        count += 1
        print 'T1 printing', count

        cv.release()
        if count == 10:
            break
    print 'T1 exiting'


def T2Processing():
    global count
    while True:
        cv.acquire()
        if count < 3 or count > 6:
            cv.notify()
        else:
            count += 1
            print 'T2 printing', count
        cv.release()
        if count >= 10:
            break
    print 'T2 exiting'



count = 0
cv = threading.Condition()

thread1 = threading.Thread(target = T1Processing, name = 'T1', args =())
thread2 = threading.Thread(target = T2Processing, name = 'T2', args =())
print 'thread1', thread1
print 'thread2', thread2
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print 'Main thread exiting'

    
    
                        
                        
