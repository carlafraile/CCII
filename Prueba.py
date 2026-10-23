v1 = 88
v2 = 'hola'
v3 = [1, 2, 3]

list1 = [v1, v2, v3]

print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[2][2])

v3.append(4)
print(list1[2])

list1.pop(2)
print(list1)

#______________________________________________________________

palabrita1 = 'Pasapalabra'
print(palabrita1[0])
print(list(palabrita1))

#______________________________________________________________

numbers = [1, 'dos', "THREE"]

for i in numbers:       # el for va leyendo elementos de la lista
    print(i)

i = 10
while i > 1:        # el while sí que puede hacer lógica
    print(i)
    i = i - 1

#______________________________________________________________

import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.sin(90)
print(b)

print(np.pi)

print(np.e)

#______________________________________________________________

