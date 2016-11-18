def find_max_letter(s):
    if len(s) == 0:
        print "The string is empty"
        return False
    count_letters = {}
    for letter in s:
        count_letters[letter] = count_letters.get(letter, 0) + 1
    max_occurrence = max(count_letters.values())
    max_letters = {key for key, value in count_letters.items() if value == max_occurrence}

    for ch in s:
        if ch in max_letters:
            return ch

s = "aaabbbcccddd"
print find_max_letter(s)
