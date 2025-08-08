import threading
import time
import Queue

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadId, threadName, q):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName
        self.q = q
    def run(self):
        print 'Starting', self.threadName
        processQueue(self.name, self.q)
        print 'Exiting', self.threadName

def processQueue(threadName, threadQ):
    while not exitFlag:
        queueLock.acquire()
        if not threadQ.empty():
            data = threadQ.get()
            print '%s processing %s' % (threadName, data)
            queueLock.release()
        else:
            queueLock.release()
        time.sleep(1)


threadList = ['thread-1', 'thread-2', 'thread-3']
nameList = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadId = 1

for tName in threadList:
    thread = myThread(threadId, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadId += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    print t
    t.join()

print 'Exiting main thread'
