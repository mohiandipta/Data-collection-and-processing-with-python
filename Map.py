#####----for Double-----####
def doubleStuff(a_list):

    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)


#####----for Triple-----####
def triple(value):
    return 3 * value

def tripleStuff(a_list):
    new_list = map(triple, a_list)
    return new_list

def quadrupleStuff(a_list):
    new_list = map(lambda value: 4 * value, a_list)
    return new_list

things =[2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)