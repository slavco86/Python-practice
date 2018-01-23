
coins = [100, 50, 20, 10, 5, 2, 1]

def give_change(amount):
    change = []
    while amount > 0:
        for coin in coins:
            if coin <= amount:
                amount -= coin
                change.append(coin)
    return change
