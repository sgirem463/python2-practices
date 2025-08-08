import threading
import time

def f1(n):
    time.sleep(5)
    print '-', n, ' '
    
    
for i in range (5):
    t = threading.Thread(target = f1, args = (i + 10, ))
    t.start()
