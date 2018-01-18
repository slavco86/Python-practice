stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,1)
        inventory[item] = inventory[item] + 1
addToInventory(stuff, dragonLoot)
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(v,end=" ")
        print(k)
    print("Total number of items: " + str(item_total))
displayInventory(stuff)