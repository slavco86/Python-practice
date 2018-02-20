
from decimal import *

coins = [1, .50, .20, .10, .05, .02, .01]

def give_change(amount):
    amount = Decimal(str(amount))
    change = []
    for coin in coins:
        coin = Decimal(str(coin))
        while coin <= amount:
            amount -= coin
            change.append(float(coin))
    return change
print(give_change(.18))
