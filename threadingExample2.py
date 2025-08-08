import time
from threading import Thread

def myfunc(i):
    print "sleeping 5 sec from thread %d" % i
    print
    time.sleep(5)
    print "finished sleeping from thread %d" % i
    print

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    print t
    t.start()
