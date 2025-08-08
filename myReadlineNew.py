

class myFile:

    def __init__(self, filename):
        self.f = open(filename)
        self.buf = ''
        self.index = 0

    def _read_256(self):
        self.buf += self.f.read(256)

    def readline(self):
        while True:
            if len(self.buf) == 0:
                self._read_256()
                print '----------'
                print 'self.buf:'
                print self.buf
                print '----------'


            offset = self.buf[self.index:].find('\n')
            if offset >= 0: # found
                line = self.buf[self.index: self.index + offset + 1]
                self.index += offset + 1
                return line
            else:
                self._read_256()
                print '=========='
                print 'self.buf:'
                print self.buf
                print '=========='                
                

                

f = myFile('bigfile')

print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
print f.readline(),
