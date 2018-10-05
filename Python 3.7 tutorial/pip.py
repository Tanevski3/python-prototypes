# def i1nitl():
#     pass
#
# def initl():
#     print 20
#     print 10
#
#
# def gpp123d():
#     print 30
#     print 60
#
# initl()
# gpp123d()
nula = 1
# nula = 'asdasdsa'
#
# print nula
#
# nula = 1.0
#
# print nula

# def processFiles(url='file://...', site='gulp', op = nula):
#     # print 'Processing '
#     print url
#
#     # print 'Site: '
#     print site
#     op = op + op
#     # print 'With operation'
#     return op
#
# print processFiles(site='file://...', 1.0)
# processFiles('asdasdads')
# processFiles('asdasdads')
# processFiles('asdasdads')
# processFiles('asdasdads',1.0)
# processFiles('asdasdads',1.0, 'nula')
# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print f(1)
# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print f(4) # [1]
# print f(2) # [1, 2]
# print f(3) # [1, 2, 3]

#
# def cheeseshop(kind,second,  *arguments, **keywords):
#     print "-- Do you have any", kind, "?"
#     print "-- Kind:", kind
#     print second
#     for arg in arguments:
#         print arg
#     print "-" * 40
#     keys = sorted(keywords.keys())
#     for kw in keys:
#         print kw, ":", keywords[kw]
#
# arr = ["good", 'ahsddsa', 1, 2 , 3]
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
#
# cheeseshop(1, *arr , **d)
#

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
#
# def asjdhjkasd(pair):
#     return pair[1]
#
# print asjdhjkasd([1, 'one'])
# pairs.sort(key=asjdhjkasd)
# print pairs

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    print 3
    pass

print my_function.__doc__
my_function()
# lambda pair: pair[1]
