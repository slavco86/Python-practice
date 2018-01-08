def collatz (number):
    if number % 2 == 0:
        number2 = number // 2
        return number2
        print(number2)
    else:
        number3 = 3*number+1
        return number3
print('Please type in any number')
x = int(input())
y = collatz(x)
while y != 1:
    collatz(y)
    y = collatz(y)
    print(y)
