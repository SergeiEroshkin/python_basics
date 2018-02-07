item_1 = float(raw_input('Please enter the price of the first item in $: '))
item_2 = float(raw_input('Please enter the price of the second item in $: '))
item_3 = float(raw_input('Please enter the price of the third item in $: '))
subtotal = item_1 + item_2 + item_3
tax = subtotal * 0.09
total = subtotal + tax
print 'SUBTOTAL:\t ' + '$' + str(subtotal)
print 'SALES TAX:\t ' + '$' + str(round(tax, 2))
print 'TOTAL:\t\t ' + '$' + str(round(total, 2))


