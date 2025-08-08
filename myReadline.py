# 



class myFile:
    def __init__(self):
        self.f = open('bigfile')
        self.buf = ''
        self.index = 0
        
    def _read_512(self):
        return self.f.read(512)

    def myReadline(self):
        while True:
            cont = False
            if (len(self.buf) == 0):
                self.buf = self._read_512()
                print '----------------------------------------------------'
                print 'self.buf:'
                print self.buf
                print '----------------------------------------------------'


                
            try:
                offset = self.buf[self.index:].index('\n')
                # print 'offest:', offset
                r = self.buf[self.index: self.index + offset + 1]
                self.index += offset + 1
                # print 'self.index', self.index
                return r
            except Exception as ex:
                print ex
                print type(ex)
                buf = self._read_512()
                self.buf = self.buf[self.index:] + buf
                print '----------------------------------------------------'
                print 'self.buf:'
                print self.buf
                print '----------------------------------------------------'
                self.index = 0
                continue # continue works
            
            print '@@@@@@@@ I am here @@@@@@@@'
            print '@@@@@@@@ I am here @@@@@@@@'

            
f = myFile()

print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
print f.myReadline(),
