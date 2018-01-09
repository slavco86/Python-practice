def convert(atr):
    newList = ''
    for i in atr:
        if atr.index(i) < len(atr)-1:
            newList += str(i) + ', '
        else:
            newList += 'and ' + str(i)
    return newList
words = []
while True:
    print('Please enter word number ' + str(len(words)+1) + '(or enter nothing to stop):')
    word = input()
    if word == '':
        print('Your collection of words is: ' + str(convert(words)))
        break
    words += [word]
