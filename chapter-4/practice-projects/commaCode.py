def comma(valList):
    sentence = ''
    for i in range(len(valList)):
        if i == len(valList) - 2: # Adds 'and' after second last item in list
            sentence = sentence + valList[i] + ' and '
        elif i == len(valList) - 1: # Adds last item without comma
            sentence += valList[i]
        else:
            sentence = sentence + valList[i] + ', ' # Adds rest of items in list with a comma and space
    return sentence

spam = ['apples', 'bananas', 'tofu', 'cats', 'lasers', 'dogs']
print(comma(spam))