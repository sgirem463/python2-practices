def hasUniqueCharacters(s):
    print s
    for i in range(len(s)):
        for c in s[i+1:]:
            if s[i] == c:
                print False     
                return False    
    print True
    return True

hasUniqueCharacters('jefferson')
hasUniqueCharacters('justin')
hasUniqueCharacters('ethan')
hasUniqueCharacters('')
