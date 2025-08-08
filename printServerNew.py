#
#
# underlying utility function get1024() which returns the next 256 bytes.
#
# print with newline '\n'
#
#

buf = ''

contents = 'kljr2hkjeklvkqekfn0239ru@931u*1nv9qefu@p91384vndlkjlkalkhlkklkjklklsdlksadlklakskdskljdlkh \
djhkjadkaslkakPP989F9C999V8ASK@NR9VN934NF943FNNF93F99EQVNF934VNFVN94394FN3P4FH934NV934F3V\
N9FN394934NVNP9439VNEFVN;KHF8SQF9438@TYI439439867908@*245709*3479GFNC9348TR90834U9RU319U49FEN\
IVNF439G93NV34GH8314FHNFI34FN349HF9034HFNI31NF394H319041NC9341HFT9H934HFGVF34FGNCJNC931HF9\
1NV139F34HF397efs897c908a7970988Y098SDVAN34G9@VWEU9QJKCNV9ERG93NV9KNKLDFLKAKKJ943GKRNK94398\
48998945698689DASFVKNKVNKJ@NKVKNFKFDNVKJNKLKNVAKDJANV*KJAERG98439NVIN49HNV9UNKKJHKhl9n;lkgr\
ne;lkv49nvkndkvnkjjf9rnvknn94nvknvjrn4g9nvkjksvlkajhfg943gkvgnekrngv9g34nvknfkhf439pnveqrn\
vkjerkjghvihg349hnvkrnkvnkkeqfj3499hklhsdkaKDHLKASHDLKHASlkdhlkasHDKAhldalkHDLAlkdakhaslkhdep982p9d\
kdklahKLDHAKLSHDLKASHDLKASHKDLKI3FOPUPODCL;KO3OOIOOJDOPSOP23UPO;KNVOP3OXKNCOEO983982Y9FH3933FVVVEEV\
EJKWKNKNFLKWIOEFOPIOPOOPpoioprienvovorejpoeoenvnerovopnveporopvopernvoernopoernvorenoenvnveqoprnvpoe\
oiewqoiheriqhvieqrhfiqewvkeqp9up934898134590870938499fv31934uvnrnngip34gp934kjvnkjsnkqKJNKLJDSKJFH9\
lkhsdkljhflksalkjlkpkgaldkg;lakdjlfkjalkasd;lkj;ls;ljsd;l4goer;j;ler;ljsdvlkjdshhkhkj\
jewhhfkewkjfkewjkjhfkljwehfklhwelkjhflkjwehklfjhewlkhlkwehqlkfhlkwehfkwklkweflkhwelklkfwelkflkfhewlkkljsdlkasdkl\
kjwefkljweklweklkewkewhlkwehkkklkPsdkkklsalk fwekl fhwelkhklklklklklllkklhlklklklfwkefweoopewoeoweew\
efwewekjkefnknvkklenklejwkljqnekljkclvnwklvenkvnkelnkvjqenkvnkjewnlkcveklklwenkjewlkrkllweqllqll\
kjekwqlkejqlkflkeqwklwelvnne;veqknvkenvo;@G4V40EVNKDFNVKDN34'

NEWLINE = '@'

def myPrint():
    buf = ''
    
    p = 0
    while True:

        if len(buf) == 0:
            buf = get256()
            if len(buf) == 0:
                print
                print 'end of program'
                print
                return

        n = buf[p:].find(NEWLINE)
        if n >= 0:
            print buf[p: p + n + 1]
            p = p + n + 1

        else: # not found, get more from input
            s = get256()
            if s == '':
                print buf[p:]
                print
                print 'end of program'
                print
                return
                
            buf = buf + s
    

    
P = 0
def get256():
    global P
    
    if len(contents[P:]) >= 256:
        s = contents[P: P + 256]
        P += 256
    else:
        s = contents[P:]
        P += len(contents[P:])
    return s


myPrint()
