def is_palindrome(word):
    # Get index of last letter in word
    last_letter = len(word) - 1
    reversed_word = ''
    # Concatenate each letter to reversed word
    for letter in word:
        reversed_word += word[last_letter]
        last_letter -= 1
    return word == reversed_word


test_string1 = 'malayalam'
test_string2 = 'malayalme'
print is_palindrome(test_string1)
print is_palindrome(test_string2)
