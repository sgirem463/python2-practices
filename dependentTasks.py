

dep = {'a': ['b', 'c'], 'b': [], 'c': [], 'd': ['c']}

tasks = dep.keys()

def removeDepT(t):
    global dep
    for d in dep:
        if t in dep[d]:
            dep[d].remove(t)

def order(tasks):
    print tasks
    if tasks == []:
        return []

    for t in tasks:
        if dep[t] == []:
            print 'found t:', t
            removeDepT(t)
            print dep
            tasks.remove(t)
            answer = [t] + order(tasks)
            return answer
    return []

print dep
print
print tasks
print

T = order(tasks)

print T

