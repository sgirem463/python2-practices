

def myAdd(a, b):
    carry = 0
    mySum = 0
    for i in range(32):
        p = 1 << i
        if ((p & a) & (p & b)):
            if carry == 0:
                carry = 1
            else:
                mySum |= p
                carry = 1
        elif ((p & a) ^ (p & b)):
            if carry == 0:
                carry = 0
                mySum |= p
            else:
                carry = 1          
        else:
            if carry == 0:
                carry = 0
            else:
                mySum |= p
                carry = 0
    return mySum

print myAdd(23, 56)
print myAdd(123, 758)
                 
             
        
