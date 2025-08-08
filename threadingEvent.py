import threading
import time

count = 0

def T1Processing():
    global count
    while True:
        ev1.wait()
        count += 1
#        ev1.clear()
        print 'T1 printing', count

        if count == 10:
            break
    print 'T1 exiting'


def T2Processing():
    global count
    while True:
        if count < 3 or count > 6:
            ev1.set()
            ev1.clear()
        else:
            count += 1
            print 'T2 printing', count
        if count >= 10:
            break
    print 'T2 exiting'



count = 0
ev1 = threading.Event()

thread1 = threading.Thread(target = T1Processing, name = 'T1')
thread2 = threading.Thread(target = T2Processing, name = 'T2')
print 'thread1', thread1
print 'thread2', thread2
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print 'Main thread exiting'
