L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []

for i in range(len(L1)):
    L3.append(L1[i] + L2[i])

print(L3)


####------using zip------####
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = []
L4 = []
L5 = list(zip(L1,L2))

for (x1, x2) in L5:
    L3.append(x1 + x2)

print(L3)
