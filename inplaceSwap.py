

def inplaceSwap():
    global a
    global b
    
    a = a - b
    b = a + b  # (a - b) + b = a
    a = b - a  # a - (a - b) = b


a = 3
b = 7

print a , b

inplaceSwap()

print a , b
