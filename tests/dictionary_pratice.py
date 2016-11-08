# Given Dictionary
stuff = {'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12}

print "Inventory"
for value, key in stuff.items():
    print value, key


def displayInventory(inventory):
    item_total = 0
    for item in stuff.items(): item_total += list(item)[1]
    return 'Total number of Items: ' + str(item_total)
print displayInventory(stuff)





