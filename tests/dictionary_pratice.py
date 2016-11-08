# Given Dictionary
stuff = {'rope': 1,
        'torch': 6,
        'gold coin': 42,
        'dagger': 1,
        'arrow': 12}

print "Inventory"
for (value, key) in zip(stuff.values(), stuff.keys()):
    print value, key

count = 0
for item in stuff.items(): count += list(item)[1]
print 'Total number of Items: ' + str(count)




