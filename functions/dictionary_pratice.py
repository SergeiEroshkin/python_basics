stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):

    print 'Inventory: '
    item_total = 0
    for value, key in inventory.items():
        print value, key
    for item in inventory.items():
        item_total += list(item)[1]
    return 'Total number of Items: ' + str(item_total)

print display_inventory(stuff)




