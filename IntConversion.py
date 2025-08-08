# interger conversion

def IntConversion(a, b):
    print a
    print b
    print '{0:064b}'.format(a)
    print '{0:064b}'.format(b)
    c = a ^ b
    print '{0:064b}'.format(c)
    oneCount = 0
    for i in range(64):
        if ((c >> i) & 1) == 1:
            oneCount += 1
    print 'oneCount:{0:0d}'.format(oneCount)


IntConversion(29, 15)


IntConversion(12345, 98765)
        
    
