dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def display_inventory(inventory):
    print 'Inventory: '
    item_total = 0
    for value, key in inventory.items():
        print value, key
    for item in inventory.items():
        item_total += list(item)[1]
    return 'Total number of Items: ' + str(item_total)

inv = add_to_inventory(inv, dragonLoot)
print display_inventory(inv)

