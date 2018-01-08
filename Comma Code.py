def convert(atr):
    newList = ''
    for i in atr:
        if atr.index(i) < len(atr)-1:
            newList += i + ', '
        else:
            newList += 'and ' + i
    return newList
words = []
while True:
    print('Please enter word number ' + str(len(words)+1) + '(or enter nothing to stop):')
    word = input()
    if word == '':
        print('Your collection of words is: ' + str(convert(words)))
        words = []
        break
    words = words + [word] 
