def URLify(s, n): # string s of size n
    print s
    s2 = ''
    for x in s:
        if x == ' ': 
            s2 += '%20' 
        else:   
            s2 += x     
    return s2

print URLify('the new web  site', 17)
s = ' a very  strange WEB P A G E '

print URLify(s, len(s))
