tableData=[['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']]

longest = 0 # to find the longest line
lines = [] # to keep lines

for elements in zip(tableData[0], tableData[1], tableData[2]):

    # join elements in line - like 'apples' + ' ' + 'Alice' + ' ' + 'dogs'
    line = ' '.join(elements)

    # add line to the list
    lines.append(line)

    #print(line) # you can print it to see what you get

    # find the longest line
    length = len(line)
    if length > longest:
        longest = length

#print('the longest:', longest)

longest += 1 # to get one space more at left side

# print lines using `%*s`
# if `longest` is 21 then it will works as `%21s`
for line in lines:
    print('%*s' % (longest, line))