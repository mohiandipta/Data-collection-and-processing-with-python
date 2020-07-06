nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]

nested1[0].append('z')
nested1[1].append('w')

print(nested1[0])
print(len(nested1))

nested1.append(['i'])
for L in nested1:
    print(L)


y = nested1[1]
print(y)
print(y[0])

print([10, 20, 30][1])
print(nested1[1][0])