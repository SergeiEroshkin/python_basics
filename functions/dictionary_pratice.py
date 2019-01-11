stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(inventory):
    """
    :param inventory: Dictionary
    :return: Sum of dictionary values
    """
    print 'Inventory: '
    for key, value in inventory.iteritems():
        print key, value
    return 'Total number of Items: {0}'.format(sum(inventory.itervalues()))


print display_inventory(stuff)




