
'''
def tryNewVar(newVar):
    try:
        newVar
    except Exception as ex:
        print type(ex)
        print ex
        newVar = 0
    else:
        newVar += 1

'''


try:
    newVar
except Exception as ex:
    print type(ex)
    print ex
    newVar = 0
else:
    newVar += 1
        

'''
tryNewVar(x)
print x
tryNewVar(x)
print x

'''
