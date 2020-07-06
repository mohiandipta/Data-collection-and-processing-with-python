nested1 = [1,2,3,['a', 'b', 'c'],4,['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1:  ")
    if type(x) is list:
        for y in x:
            print("    level2: {}".format(y))
    else:
        print(x)    