def is_palindrome(word):
    #return s == s[::-1]
    letter_in_word = len(word) - 1
    # Lets make backward of input word
    rev_word = ''
    for letter in word:
        rev_word += word[letter_in_word]
        letter_in_word -= 1
    return word == rev_word


test_string1 = 'malayalam'
test_string2 = 'malayalme'
print is_palindrome(test_string1)
print is_palindrome(test_string2)
