dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


def add_to_inventory(inventory, added_item):
    for item in added_item:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def display_inventory(inventory):
    print '*** Inventory ***'
    for k, v in inventory.items():
        print k, v
    return 'Total number of items is ' + str(sum(inventory.values()))


print display_inventory(add_to_inventory(inv, dragonLoot))

