from collections import deque

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))
fruits.reverse()
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)
fruits.append('pear')
print(fruits)

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
queue.popleft()
print(queue)

squares = []

for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))

print(squares)

squares = [x**2 for x in range(10)]

print(squares)

list_1 = [(1),2]
list_2 = [3, 4]

combined_list = list_1 + list_2

print(combined_list)

combined_list = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(combined_list)

b = 'babanana aaa a    '

print(b.strip() + 'X')

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]

print(a)

del a[2:4]

print(a)

del a[:]

print(a)

del a

# print(a) - error will occur

def transpose_matrix(matrix):
    length = len(matrix[0])
    print (length)
    return [[row[i] for row in matrix] for i in range(length)]
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
print(transpose_matrix(matrix))

t = 1234, 5678, 'yuple'
print(t)
u = t, (1,2)
print(u)

x, y, z = t

print(x)
print(y)
print(z)
