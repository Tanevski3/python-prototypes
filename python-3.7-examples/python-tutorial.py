# x = int(input("Please inter integer"))
#
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# else:
#     print('Other')

range(5)

for n in range(2, 10):
     for x in range(2, n):
         print x
         if n % x == 0:
             print n, 'equals', x, '*', n/x
             break
     else:
         # loop fell through without finding a factor
         print n, 'is a prime number'


n = 2
  x= []
