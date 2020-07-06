nested1 = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    for y in x:
        print("     level2: " + y)


#####-----Selective alphabate-----#####
L = [['apples','bananas','oranges','blueberries','lemons'],['carrots','cucumbers','root beer','cranberry juice','green beens']]
b_strings = []
for lst in L:
    for word in lst:
        if 'b' in word:
            b_strings.append(word)
    print(b_strings)
        