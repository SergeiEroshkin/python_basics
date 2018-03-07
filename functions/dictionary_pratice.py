stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    """
    :param inventory: Dictionary
    :return: Sum of dictionary values
    """
    print 'Inventory: '
    for value, key in inventory.iteritems():
        print value, key
    return 'Total number of Items: ' + str(sum(inventory.itervalues()))


print display_inventory(stuff)




