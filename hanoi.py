# Hanoi tower


towers = ['A', 'B', 'C']

def hanoi(n, s, d, third): # number of disks, source, destination, the thrid tower
    if n == 1:
        print 'move %d from %s to %s' % (n, s, d)
        return
    hanoi(n - 1, s, third, d)
    print 'move %d from %s to %s' % (n, s, d)
    hanoi(n - 1, third, d, s)







hanoi(3, 'A', 'C', 'B')
    
