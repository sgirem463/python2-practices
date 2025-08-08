def string_permutation(p, q):
        print p
        print q
        if len(p) != len(q):
                return False
        for i in range(len(p)):
                if p[i] not in q:
                        return False
                else:
                        # p = p[1:]
                        index = q.index(p[i])
                        q = q[:index] + q[index + 1:]
        return True

print string_permutation('abcd', 'dcab')
print
print string_permutation('abcd', 'dcaa')
print
print string_permutation('', '')
print
print string_permutation('abcd', 'dcaba')
print
print string_permutation('abwczxbmyawad', 'madycxawbazwb')
